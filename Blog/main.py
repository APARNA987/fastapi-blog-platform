#  main requirements

# Your Requirements Recap
# Users can sign up and log in

# Logged-in users can create, edit, delete their own blog posts

# Everyone (even not logged in) can view posts

# Each blog post belongs to one user

from fastapi import FastAPI
from .routers import user_router, blog_router, authentication
from Blog.database import engine
from Blog.model_name import models 

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(user_router.router)
app.include_router(blog_router.router)
app.include_router(authentication.router)


# check for current user id , owner id for delete blog. 