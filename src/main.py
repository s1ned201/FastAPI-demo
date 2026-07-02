from fastapi import FastAPI
from src.core.router import router


app = FastAPI(title="FastAPI-demo Docs")

app.include_router(router)


# class ItemPart(BaseModel):
#     name: str
#     description: str
#
#
# class Item(BaseModel):
#     name: str
#     description: str
#     price: float
#     tax: float | None = None
#     item_parts: list[ItemPart] | None = None
#
# item_parts = [
#     {
#         "name": "part1",
#         "description": "description1",
#     },
#     {
#         "name": "part2",
#         "description": "description2",
#     }
# ]
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}