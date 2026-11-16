from fastapi import APIRouter, status, Depends, HTTPException, Form
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas
from app.security import hash_password, verify_password, create_access_token, get_current_user, require_role


router = APIRouter(prefix= "/auth", tags= ["Authentication"])


# ============== > Post Register < ================
@router.post("/", response_model=schemas.UserResponse, status_code = status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user= db.query(models.User).filter(models.User.email == user.email).first()
    
    if existing_user:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail = "Email is already registered"
        )
        
    hashed_password = hash_password(user.password)
    
    db_user = models.User(
        name = user.name,
        email= user.email,
        hashed_password = hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

# ================ > Login User < =====================
@router.post("/login", response_model=schemas.Token)
def login_user(
    username: str = Form(),
    password: str = Form(),
    db: Session = Depends(get_db)
):
    db_user = db.query(models.User).filter(
        models.User.email == username
    ).first()

    if not db_user or not verify_password(
        password, db_user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={"sub": str(db_user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
    
@router.get("/me", response_model=schemas.UserResponse)
def get_me(
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    current_user = db.query(models.User).filter(
        models.User.id == int(user_id)
    ).first()

    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return current_user

@router.get("/admin-test")
def admin_test(
    current_user: models.User = Depends(require_role(["admin"]))
):
    return {
        "message": "Welcome Admin!",
        "user": current_user.name,
        "role": current_user.role
    }
    
@router.get("/manager-test")
def manager_test(
    current_user: models.User = Depends(
        require_role(["admin", "manager"])
    )
):
    return {
        "message": "Welcome Admin or Manager!",
        "user": current_user.name,
        "role": current_user.role
    }