from fastapi import FastAPI

from user import router as user_router
from organisation import router as organisation_router

app = FastAPI()

app.include_router(user_router)
app.include_router(organisation_router)
@app.get("/")
def home():
    return{
        "message":"welcome to the student  and  oraganisation API"
        
    }