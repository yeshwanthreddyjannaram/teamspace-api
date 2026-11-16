from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas
from app.security import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# ============== > Create Task < ==============
@router.post(
    "/",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    
    project = db.query(models.Project).filter(
        models.Project.id == task.project_id,
        models.Project.owner_id == int(current_user_id)
    ).first()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )

    
    if task.assigned_to is not None:

        

        assignee = db.query(models.User).filter(
            models.User.id == task.assigned_to
        ).first()


        if not assignee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Assigned user not found"
            )

    
    new_task = models.Task(
        title=task.title,
        description=task.description,
        project_id=task.project_id,
        assigned_to=task.assigned_to,
        due_date=task.due_date
    )

    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

# ============== > Get All Tasks < ==============
@router.get("/", response_model=list[schemas.TaskDetailsResponse])
def get_tasks(
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    tasks = db.query(models.Task).join(
        models.Project
    ).filter(
        models.Project.owner_id == int(current_user_id)
    ).all()

    return tasks

# ============== > Update Task < ==============
@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    task_data: schemas.TaskUpdate,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    
    task = db.query(models.Task).join(models.Project).filter(
        models.Task.id == task_id,
        models.Project.owner_id == int(current_user_id)
    ).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    
    if task_data.assigned_to is not None:
        assignee = db.query(models.User).filter(
            models.User.id == task_data.assigned_to
        ).first()

        if not assignee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Assigned user not found"
            )

    
    task.title = task_data.title
    task.description = task_data.description
    task.assigned_to = task_data.assigned_to
    task.due_date = task_data.due_date
    task.status = task_data.status

    
    db.commit()
    db.refresh(task)

    return task

# ============== > Get Task By ID < ==============
@router.get("/", response_model=list[schemas.TaskDetailsResponse])
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    task = db.query(models.Task).join(
        models.Project
    ).filter(
        models.Task.id == task_id,
        models.Project.owner_id == int(current_user_id)
    ).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task

# ============== > Delete Task < ==============
@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    task = db.query(models.Task).join(
        models.Project
    ).filter(
        models.Task.id == task_id,
        models.Project.owner_id == int(current_user_id)
    ).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted successfully"
    }