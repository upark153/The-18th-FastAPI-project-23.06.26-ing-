from typing import Union

from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello" : "World"}
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# app = FastAPI()

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
#     if model_name == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
    
#     return {"model_name" : model_name, "message": "Have some residuals"}


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{itme_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name" : item.name, "item_id": item_id}
