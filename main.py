from fastapi import FastAPI
from endpoints.user import userRouter
from endpoints.parcelas import parcelasRouter
from endpoints.activities import activitiesRouter

app = FastAPI()

app.include_router(userRouter)

app.include_router(parcelasRouter)

app.include_router(activitiesRouter)