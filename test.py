import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "Current date and time": datetime.datetime.now()}