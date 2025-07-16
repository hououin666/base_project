import uvicorn
from fastapi import FastAPI, APIRouter
from api import router as api_router
from core.config import settings

app = FastAPI()
app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host=settings.run.host, port=settings.run.port)
