from fastapi import APIRouter, FastAPI

router = APIRouter()

@router.get("/tasks")
async def list_task():
    pass

@router.post("/tasks")
async def create_task():
    pass

@router.put("/tasks/{task_id}")
async def update_task():
    pass

@router.delete("/tasks/{task_id}")
async def delete_task():
    pass