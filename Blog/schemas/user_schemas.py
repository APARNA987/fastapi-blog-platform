# user create (when user sends data to register)
# user response(when you sends data back to the user)

from pydantic import BaseModel
from typing import Optional

# User input when signing up
class UserCreate(BaseModel):
    username: str
    email: str
    password: str


# Response after registration or fetching user info
class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

# updating user's profile
class UserUpdate(BaseModel): # why needed it alag se is because while creaating profile everykeyword is mandatory but that is not the case while updating so user can update a single thing and that's all.
    username: Optional[str]=None
    email: Optional[str]=None
    password: Optional[str]=None