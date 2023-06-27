from typing import Union, List
from uuid import UUID, uuid4

from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

from models import User, Gender, Role

app = FastAPI() # 인스턴스화. 

db: List[User] = [
    User(
        # id=uuid4(), 
        id=UUID("ff8b7797-037a-42d4-8b29-8ee51edae0b5"),
        first_name="Uiyong", 
        last_name="Park",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        # id=uuid4(), 
        id=UUID("ab281d2b-f251-4b0c-b9fc-70cca45c32b4"),
        first_name="hanyong", 
        last_name="Park",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/") # get은 http 메서드. () 경로
async def root():
    return {"Hello" : "World"} # 반환하는 값. JSON Object. 키 : Hello 값 : World 

@app.get("/api/v1/users")
async def fetch_users():
    return db;







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
