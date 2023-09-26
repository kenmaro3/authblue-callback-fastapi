from fastapi import FastAPI

from pydantic import BaseModel


class Callback(BaseModel):
    log_id: str
    created_at: str
    client_name: str
    uid: str


app = FastAPI()


@app.get("/")
async def root():
    print("HERE!!")
    return {"message": "Hello World"}


@app.post("/callback")
async def create_item(callback_log: Callback):
    print("got it here\n")
    print(callback_log)
    return callback_log
