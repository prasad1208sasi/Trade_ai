from fastapi import Header, HTTPException
import os

API_TOKEN ='abc'

def verify_token(Authorization: str = Header(None)):
    if Authorization != API_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"user": "valid_user"}