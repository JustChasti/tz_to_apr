import uvicorn
from fastapi import FastAPI
from loguru import logger
from searcher.views import search_router


app = FastAPI()
logger.add("test.log", rotation="100 MB")


app.include_router(search_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
