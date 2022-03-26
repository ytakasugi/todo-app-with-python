from typing import Optional
from pydantic import BaseModel, Field

# titleのみを持つベースクラス。
# 他のクラスは、このクラスを継承する
class TaskBase(BaseModel):
    title: Optional[str] = Field(None)

# このクラスは、id、title、doneの3つのフィールドを持つ。
class Task(TaskBase):
    id: int
    # デフォルト値は、None
    title: Optional[str] = Field(None)
    # デフォルト値は、False
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
