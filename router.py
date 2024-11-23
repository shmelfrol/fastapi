from typing import Annotated
from fastapi import APIRouter, Depends

from repo import TaskRepo
from schema import STask, STaskAdd, STaskId

router = APIRouter(
    prefix="/tasks",
)

@router.get("")
async def get_tasks()-> list[STask]:
    tasks = await TaskRepo.find_all()
    return tasks



tasks = []

@router.post("")
async def add_task(
    task:Annotated[STaskAdd, Depends()],
)-> STaskId:
    task_id = await TaskRepo.add_one(task)
    return {"ok":True, "task_id": task_id}