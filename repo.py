from sqlalchemy import select
from db import TaskOrm, new_session
from schema import STaskAdd, STask



class TaskRepo:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id
        
    @classmethod
    async def find_all(cls)-> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            print(task_models)
            tasks = [STask.model_validate(task_model) for task_model in task_models]
            return tasks
            
            
            
