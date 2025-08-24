from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError
from sqlalchemy.orm import Session
from Blog.database import get_db
from Blog.model_name import models
from fastapi.security import OAuth2PasswordBearer
import Blog.JWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user_id = Blog.JWT.verify_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == user_id).first()
    print(user, "jnfuirnfuir4furgf")
    return user


 # this function works after the authentication, Extract and verify the JWT token from the request, Decode the token to get the user’s identity (like user_id).

# Query the database to fetch the full user object.

# Return the authenticated User so it can be used in protected routes.