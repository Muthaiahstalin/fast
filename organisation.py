from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
router = APIRouter()
organis={}
class Organisation(BaseModel):
    name:str
    address:str
    no_of_employees:int
    no_of_departments:int
    no_of_projects:int
    no_of_clients:int
@router.post("/organis")
def create(org_id:str,org:Organisation):
    if org_id in organis:
        raise HTTPException(
            status_code=404,
            detail="Organisation ID already exists"
        )
    organis[org_id]=org.model_dump()
    return{
        "message":"Organisation details added succesfully",
            "org_id":org_id,
            "organisation":organis[org_id]
            }

@router.get("/organis")
def read():
    return organis

@router.get("/organis/{org_id}")
def get(org_id:str):
    if org_id not in organis:
        raise HTTPException(
            status_code=404,
            detail="Organisation not found"
        )
    return organis[org_id]



@router.put("/organis/{org_id}")
def update(org_id:str, organisation:Organisation):
    if org_id not in organis:
        raise HTTPException(
            status_code=404,
            detail="Organisation not found"
        )
    organis[org_id]=organisation.model_dump()
    return {
        "message":"Organisation details updated successfully",
          "org_id":org_id,
          "organisation":organis[org_id]
             }

@router.delete("/organis/{org_id}")
def delete(org_id:str):
    if org_id not in organis:
        raise HTTPException(
            status_code=404,
            detail="Organisation not found"
        )
    del organis[org_id]
    return{
        "message":"organisation {org_id} deleted successfully"
    }

    