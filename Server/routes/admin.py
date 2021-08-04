from fastapi import APIRouter, Depends, HTTPException, Header
from dependencies.is_admin_role import is_admin_role

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(is_admin_role)]
)

@router.get("")
async def read_item():
    return "Hello admin"