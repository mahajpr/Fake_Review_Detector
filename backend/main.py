from fastapi import FastAPI
from database.db import engine, Base
from routes.routes import router
from models import tables 

app = FastAPI(title="Fake Review Detection explanation tool")

Base.metadata.create_all(bind=engine)

app.include_router(router)
