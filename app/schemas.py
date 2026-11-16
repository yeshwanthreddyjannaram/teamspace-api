from pydantic import BaseModel, Field, EmailStr
from typing import Literal
from datetime import date

# ============== > User Registration < ===============
class UserCreate(BaseModel):
    name : str = Field(min_length= 2, max_length= 100)
    email : EmailStr
    password : str = Field(min_length= 8, max_length= 128)
    

# ============== > User Response < ===============
class UserResponse(BaseModel):
    id : int
    name : str
    email : EmailStr
    role : str
    
    model_config= {"from_attributes": True}
    
# ============== > User Login < =================
class UserLogin(BaseModel):
    email : EmailStr
    password : str
    
# =============== > User Token < ================
class Token(BaseModel):
    access_token : str
    token_type : str
    
# ============== > Project Creation < ===============
class ProjectCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: str | None = None


# ============== > Project Response < ===============
class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str | None
    owner_id: int

    model_config = {"from_attributes": True}
    
# ============== > Task Creation < ==============
class TaskCreate(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    description: str | None = None
    project_id: int
    assigned_to: int | None = None
    due_date: date | None = None


# ============== > Task Response < ==============
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    due_date: date | None
    project_id: int
    assigned_to: int | None

    model_config = {"from_attributes": True}
    
    
# ============== > Task Update < ==============
class TaskUpdate(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    description: str | None = None
    assigned_to: int | None = None
    due_date: date | None = None
    status: Literal["pending", "in_progress", "completed"] = "pending"
    
# =============== > Project Response < ==================
class ProjectWithTasksResponse(BaseModel):
    id: int
    name: str
    description: str | None
    owner_id: int
    tasks: list[TaskResponse]

    model_config = {"from_attributes": True}

# ============ > Project Owner Response < ============
class ProjectOwnerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = {"from_attributes": True}
    
    
# ================ > Project Details Response < ==================
class ProjectDetailsResponse(BaseModel):
    id: int
    name: str
    description: str | None
    owner_id: int
    owner: ProjectOwnerResponse
    tasks: list[TaskResponse]

    model_config = {"from_attributes": True}
    
    
# =============== > Task Details Response < ===============  
class TaskDetailsResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    due_date: date | None
    project: ProjectResponse
    assignee: ProjectOwnerResponse | None

    model_config = {"from_attributes": True}

