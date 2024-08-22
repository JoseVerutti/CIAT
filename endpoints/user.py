from fastapi import APIRouter
from schemas.user import User
from config.db import dynamodb as db
from functions.user import *

userRouter = APIRouter()

@userRouter.get("/user/{id}", tags=["users"])
def getUser(id:str):
    response = obtenerUsuarioID(db, id)
    return {"content":response}

@userRouter.get("/user", tags=["users"])
def getAll():
    response = obtenerUsuarios(db)
    return {"content":response}

@userRouter.post("/user", tags=["users"])
def postUser(user: User):
    response = agregarUsuario(db, user)
    return {"content":response}
    



    