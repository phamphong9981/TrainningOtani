from fastapi import Header, HTTPException,status


async def is_admin_role(token: str = Header(...)):
    if token != "token_admin_hashed":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Login with admin role fail")