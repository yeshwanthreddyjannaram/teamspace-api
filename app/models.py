
from sqlalchemy import Column, String, Integer, Text, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.database import Base


# =========== > User Table < ==========
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String(20), default="member", nullable=False)

    
    projects = relationship("Project", back_populates="owner")

    assigned_tasks = relationship(
        "Task",
        back_populates="assignee",
        foreign_keys="Task.assigned_to"
    )


# ============ > Project Table < ===========
class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)

    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    
    owner = relationship("User", back_populates="projects")

    tasks = relationship("Task", back_populates="project")


# ============= > Task Table < ===============
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(20), default="pending", nullable=False)
    due_date = Column(Date, nullable=True)

    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)

    project = relationship("Project", back_populates="tasks")

    assignee = relationship(
        "User",
        back_populates="assigned_tasks",
        foreign_keys=[assigned_to]
    )
