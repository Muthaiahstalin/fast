from fastapi import APIRouter ,HTTPException
from pydantic import BaseModel
router = APIRouter()
user={}
class Employee(BaseModel):
    name:str
    age:int
    department:str

@router.post("/user")
def create(user_id:str,employee:Employee):
    if user_id in user:
        raise HTTPException(
            status_code=404,
            detail="user already exists"
        )
    user[user_id]=employee.model_dump()
    return{
        "message":"user added successfully",
        "user_id":user_id,
        "user":user[user_id]
    }

@router.get("/user")
def read():
    return user
@router.get("/user/{user_id}")
def get(user_id:str):
    if user_id not in user:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return user[user_id]

@router.put("/user/{user_id}")
def update(user_id:str,employee:Employee):
    if user_id not in user:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    user[user_id]=employee.model_dump()
    return{
        "message":"user details updated successfully",
            "user_id":user_id,
             "user":user[user_id]
          }

@router.delete("/user/{user_id}")
def delete(user_id:str):
    if user_id not in user:
        raise HTTPException (
            status_code=404,
            detail="user not found"
        )
    del user[user_id]
    return {
        "message":"user {user_id} deleted successfully"
    }