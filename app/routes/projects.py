from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas
from app.security import get_current_user

router = APIRouter(prefix="/projects", tags=["Projects"])

# ============== > Create Project < ==============
@router.post(
    "/",
    response_model=schemas.ProjectResponse,
    status_code=status.HTTP_201_CREATED
)
def create_project(
    project: schemas.ProjectCreate,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    new_project = models.Project(
        name=project.name,
        description=project.description,
        owner_id=int(current_user_id)
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project

# ============== > Get All Projects < ==============
@router.get(
    "/",
    response_model=list[schemas.ProjectResponse]
)
def get_projects(
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    projects = db.query(models.Project).filter(
        models.Project.owner_id == int(current_user_id)
    ).all()

    return projects

# ============== > Get Project By ID < ==============
@router.get(
    "/{project_id}",
    response_model=schemas.ProjectDetailsResponse
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    project = db.query(models.Project).filter(
        models.Project.id == project_id,
        models.Project.owner_id == int(current_user_id)
    ).first()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )

    return project

# ============== > Update Project < ==============
@router.put(
    "/{project_id}",
    response_model=schemas.ProjectResponse
)
def update_project(
    project_id: int,
    project_data: schemas.ProjectCreate,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    project = db.query(models.Project).filter(
        models.Project.id == project_id,
        models.Project.owner_id == int(current_user_id)
    ).first()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )

    project.name = project_data.name
    project.description = project_data.description

    db.commit()
    db.refresh(project)

    return project

# ============== > Delete Project < ==============
@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    project = db.query(models.Project).filter(
        models.Project.id == project_id,
        models.Project.owner_id == int(current_user_id)
    ).first()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )

    db.delete(project)
    db.commit()

    return {
        "message": "Project deleted successfully"
    }