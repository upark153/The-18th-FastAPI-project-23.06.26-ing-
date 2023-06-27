# pydantic 데이터 유효성 검사를 수행하는 python 라이브러리
# 속성이 있는 클래스로 데이터의 모양을 선언할 수 있다.

from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum # 열거형

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender : Gender
    roles: List[Role]