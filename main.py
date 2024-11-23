
from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager
from db import create_tables, delete_tables
from router import router as tasks_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('db cleaned')
    await create_tables()
    print('db created')
    yield
    print('power off')
        

app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router)




