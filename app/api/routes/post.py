from fastapi import  APIRouter , Depends
from app.db.models.post import Post
from app.schemas.post import PostCreate , PostResponse
from app.api.dependencies.auth import get_current_user
from app.db.models.user import User
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter()

@router.post('/posts' , response_model=PostResponse)
def create_post(
    post : PostCreate,
    current_user : User = Depends(get_current_user),
    db : Session = Depends(get_db)
):
    new_post = Post(
        content = post.content,
        user_id = current_user.id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post



@router.get('/posts' , response_model=list[PostResponse]) #as we are going to return all posts , soo we will have a list of post responses
def get_all_posts(
    db : Session = Depends(get_db)
):
    posts = db.query(Post).all()
    return posts