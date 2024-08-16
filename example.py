from fastapi import FastAPI, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

api_keys = [
    "akljnv13bvi2vfo0b0bw"
]  # This is encrypted in the database

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # use token authentication


def api_key_auth(api_key: str = Depends(oauth2_scheme)):
    if api_key not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )


app = FastAPI()


@app.get("/protected", dependencies=[Depends(api_key_auth)])
def add_post() -> dict:
    return {
        "data": "You used a valid API key."
    }


####################################


# call API
import requests

url = "http://localhost:8000/protected"

# The client should pass the API key in the headers
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer akljnv13bvi2vfo0b0bw'
}

response = requests.get(url, headers=headers)
print(response.text)  # => "You used a valid API key."
