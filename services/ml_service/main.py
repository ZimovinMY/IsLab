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
    buckets=(100000, 1000000, 3000000, 5000000, 15000000, 50000000, 100000000)
)

@app.get('/')
def root_dir():
    return({'Hello': 'world'})  

@app.post('/api/prediction')
def make_prediction(id: int, item_features: dict):
    prediction = app.handler.predict(item_features)
    return ({
             'car_id': id,
             'price': prediction
            })