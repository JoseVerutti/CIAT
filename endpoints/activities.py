from fastapi import APIRouter
from functions.activities import *
from config.db import dynamodb as db
from schemas.activities import Activities

activitiesRouter = APIRouter()


@activitiesRouter.get("/user/activities/{id}", tags=["actividades"])
def getParcela(id:str):
    response = obtenerActividades(db, id)
    return {"content":response}


@activitiesRouter.post("/user/activities", tags=["actividades"])
def postParcela(actividad: Activities, id:str):
    actividad.fecha = str(actividad.fecha)
    response = agregarActividad(db, actividad, id)
    return {"content":response}