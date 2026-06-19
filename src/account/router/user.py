from fastapi import APIRouter




router = APIRouter(
    prefix="/users",
    tags=["Account"],
)

@router.get("/")
def read_users():
    return [{"name": "Doc Brown"}, {"name": "Marty McFly"}]
