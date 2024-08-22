from fastapi import APIRouter
from schemas.parcelas import Parcelas
from functions.parcelas import *
from config.db import dynamodb as db

parcelasRouter = APIRouter()


@parcelasRouter.get("/user/parcelas/{id}", tags=["parcelas"])
def getParcela(id:str):
    response = obtenerParcelas(db, id)
    return {"content":response}


@parcelasRouter.post("/user/parcelas", tags=["parcelas"])
def postParcela(parcela: Parcelas, id:str):
    response = agregarParcela(db, parcela, id)
    return {"content":response}