"""Secrets API"""

import yaml
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class RequestFormat(BaseModel):
    """Request Format for the API request"""

    token: str


@app.get("/")
async def main():
    """Get API Status"""
    return True


@app.get("/secret")
def get_secret(request: RequestFormat):
    """Retrieve the secret for the requested token"""
    with open("./creds/creds.yml", "r", encoding="utf-8") as ymlfile:
        data = yaml.safe_load(ymlfile)
        try:
            return data[request.token]
        except KeyError as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No secret found for the token",
            ) from exc
