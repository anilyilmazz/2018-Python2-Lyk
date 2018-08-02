from celery import Celery
import json

app = Celery(__name__, backend="amqp://localhost", broker="redis://localhost")

parse_list=[]

@app.task
def multiple(x,y):
    z = x**y
    print(z)
    return z

@app.task()
def parse_date(data):
    parse_list.append({"kelime":data,"parse":data.split(" ")})
    print(json.dumps(parse_list))


