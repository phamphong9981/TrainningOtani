from fastapi import Header, HTTPException,status
import jwt

import crud


async def is_valid_account(token: str = Header(...)):
    try:
        jwt.decode(token, "secret", algorithms=["HS256"])["name"]
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalid")