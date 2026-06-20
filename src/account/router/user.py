
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.account.services.user import UserNotfound
from src.account.schemas.user import UserCreateSchema, UserResponseSchema
from src.account.services.user import UserService, UserAlreadyExist
from src.core.database import get_sync_session

router = APIRouter(
    prefix="/users",
    tags=["Account"],
)

# @router.get("/")
# def read_users():
#     return [{"name": "Doc Brown"}, {"name": "Marty McFly"}]


@router.post(
    path="/",
    response_model=UserResponseSchema,
    status_code=201
)
def create_user(
        user_schema: UserCreateSchema,
        session: Session = Depends(get_sync_session)
):
    try:
        user_service = UserService(session)
        return user_service.create(user_schema=user_schema)
    except UserAlreadyExist:
        raise HTTPException(status_code=403, detail="User already exists")

@router.get(
    path="/{user_id}",
    response_model=UserResponseSchema,
    status_code=200
)
def get_user(
        user_id: int,
        session: Session = Depends(get_sync_session)
):
    try:
        user_service = UserService(session)
        return user_service.get_one(user_id=user_id)
    except UserNotfound:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

@router.get(
    path="/",
    response_model=list[UserResponseSchema],
    status_code=200
)
def get_all_users(
        session: Session = Depends(get_sync_session)
):
    user_service = UserService(session)
    return user_service.get_all()

@router.put(
    path="/{user_id}",
    response_model=UserResponseSchema,
    status_code=200
)
def update_user(
        user_id: int,
        user_schema: UserCreateSchema,
        session: Session = Depends(get_sync_session)
):
    try:
        user_service = UserService(session)
        return user_service.update(user_id=user_id, user_schema=user_schema)
    except UserNotfound:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

@router.delete(
    path="/{user_id}",
    status_code=204
)
def delete_user(
        user_id: int,
        session: Session = Depends(get_sync_session)
):
    try:
        user_service = UserService(session)
        return user_service.delete(user_id=user_id)
    except UserNotfound:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")