import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "timestamp": datetime.datetime.now()}