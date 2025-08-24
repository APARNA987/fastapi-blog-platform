from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Blog.database import SessionLocal
from Blog.model_name import models
from Blog.database import get_db 
from Blog.schemas import blog_schemas, user_schemas
from Blog.Oauth import get_current_user



router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)


# POST /blogs → Create a blog
@router.post("/",status_code = status.HTTP_201_CREATED, response_model=blog_schemas.BlogResponse)
def create_blog(blog: blog_schemas.BlogCreate, db: Session = Depends(get_db), current_user: user_schemas.UserCreate = Depends(get_current_user)):
    print("current user :       ", current_user)
    db_blog = models.Blog(title = blog.title, content = blog.content,owner_id=current_user.id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


# GET /blogs → Get all blogs
@router.get("/", response_model=list[blog_schemas.BlogResponse])
def get_blogs(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()

# GET /blogs/{id} → Get blog by ID
@router.get("/{id}", response_model=blog_schemas.BlogResponse)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


# edit the blog

@router.put("/{id}", response_model=blog_schemas.BlogResponse)
def update_blog(id: int, blog: blog_schemas.BlogCreate, db: Session = Depends(get_db), current_user: user_schemas.UserResponse = Depends(get_current_user)):
    db_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not db_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    if db_blog.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this blog")

    db_blog.title = blog.title
    db_blog.content = blog.content
    db.commit()
    db.refresh(db_blog)
    return db_blog


# deleting a blog
@router.delete("/{id}")
def delete_blog(id: int, db: Session = Depends(get_db), current_user: user_schemas.UserResponse = Depends(get_current_user)):
    db_blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not db_blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    if db_blog.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this blog")

    db.delete(db_blog)
    db.commit()
    return {"message": "Blog deleted successfully"}
