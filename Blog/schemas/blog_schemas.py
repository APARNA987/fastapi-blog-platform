# user create (when user sends data to register)
# user response(when you sends data back to the user)

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from .user_schemas import UserResponse

# Input when creating or updating a blog post
class BlogCreate(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True

#Response when getting a blog post
class BlogResponse(BaseModel): # is controls what data is returned when someone asks to view blog posts
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    owner_id: int  #  <--- So client knows who owns this blog ....owner_id is a foreign key in the Blog model that links each blog post to a user (who is the author/owner of that blog).

    class Config:
        orm_mode = True


# to return blog post along with author info
class BlogWithAuthor(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    owner: UserResponse  # nested schema

    class Config:
        orm_mode = True
