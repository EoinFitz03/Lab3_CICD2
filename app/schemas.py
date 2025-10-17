# app/schemas.py
from pydantic import BaseModel, EmailStr, constr, conint

class User(BaseModel):
    user_id: int
    student_id: constr(pattern=r'^S\d{7}$')
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    age: conint(gt=18)

class update_user(BaseModel):
    user_id: int
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    age: conint(gt=18)

class Delete_user(BaseModel):
    user_id: int
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    age: conint(gt=18)

class Health_user(BaseModel):
    health_id: int
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    age: conint(gt=18)