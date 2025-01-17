from typing import Optional
from pydantic import BaseModel

class ReviewBase(BaseModel):
  id: Optional[int]
  body: Optional[str]
  product_id: Optional[int]
  user_id: Optional[int]
  created_at: Optional[datetime.datetime]


class ReviewCreate(BaseModel):
  user_id: int
  body: str
  product_id: int


class ReviewUpdate(BaseModel):
  body: str



