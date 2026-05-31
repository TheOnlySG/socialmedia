from fastapi import Depends
from app.db.database import get_db
from app.db.models.post import Post
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

def get_post_by_id(
        id : int,
        db : Session 
):
    single_post = db.query(Post).filter(
        Post.id == id 
    ).first()

    if not single_post:
        raise HTTPException(
            status_code=404, 
            detail='Post Not Found'
        )

    return single_post