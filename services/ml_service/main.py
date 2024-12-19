from fastapi import FastAPI
from api_handler import FastAPIHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram, Gauge, Counter, Summary

app = FastAPI()
app.handler = FastAPIHandler()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

prediction_metric = Histogram(
    'prediction_metric_histogram',
    'histogram of predicted prices',
    buckets=(1, 5, 10, 15, 25, 50, 100)
)

@app.get('/')
def root_dir():
    return({'Hello': 'world'})  

@app.post('/api/prediction')
def make_prediction(id: int, item_features: dict):
    prediction = app.handler.predict(item_features)
    prediction_metric.observe(prediction)
    return ({
             'car_id': id,
             'price': prediction
            })