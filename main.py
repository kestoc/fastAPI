from typing import Union

from fastapi import FastAPI

import requests

from pydantic import BaseModel # adicionar en los imports en el main.py

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

URL = 'https://62fdb8436e617f88deadb331.mockapi.io/items'

@app.get("/items")
def read_root():
    response = requests.get(URL, {}, timeout=5)
    return {"items": response.json() }

@app.put("/items/{item_id}")
def put_data(item_id : int, item : Item):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = requests.put(URL+"/"+str(item_id), item.json(), headers=headers)
    return {"items": response.json() }

@app.post("/items/")
def post_data(item : Item):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(URL, item.json(), headers=headers)
    return {"items": response.json() }

@app.delete("/items/{item_id}")
def delete_data(item_id : int):
    response = requests.delete(URL+"/"+str(item_id))
    return {"items": response.json() }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}