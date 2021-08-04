from fastapi import Header, HTTPException,status
import jwt

async def is_admin_role(token: str = Header(...)):
    try:
        if jwt.decode(token, "secret", algorithms=["HS256"])["role"] != 1:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Login with admin role fail")
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalid")