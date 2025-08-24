from fastapi import APIRouter, status, Depends, HTTPException
from Blog.model_name import models
from Blog.schemas import user_schemas
from sqlalchemy.orm import Session
from Blog.database import get_db 
from passlib.context import CryptContext
from Blog.Oauth import get_current_user

router = APIRouter(prefix = "/users",tags = ["Users"])

#hashing password for security
pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated = "auto")

def hash_password(password):
    return pwd_cxt.hash(password)

# POST /users → Register a new user
@router.post("/", status_code = status.HTTP_201_CREATED, response_model = user_schemas.UserResponse)
def User(request: user_schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(request.password)
    new_user = models.User(username=request.username, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# GET /users → Get all users
@router.get("/", response_model=list[user_schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# GET /users/{id} → Get user by ID
@router.get("/{id}", response_model=user_schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update the user's profile

@router.put("/{id}", response_model=user_schemas.UserResponse)
def update_user(id: int, request: user_schemas.UserUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if current_user.id != id:
        raise HTTPException(status_code=403, detail="Not authorized to update this profile")
    if request.username is not None:
        user.username = request.username

    if request.email is not None:
        user.email = request.email

    if request.password is not None:
        user.password = hash_password(request.password)

    db.commit()
    db.refresh(user)
    return user

