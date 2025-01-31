from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.admin_models import Admin
from pydantic import BaseModel

router = APIRouter()
india_timezone = timezone(timedelta(hours=5, minutes=30))

# Define LoginRequest model for validation
class LoginRequest(BaseModel):
    email: str
    password: str

class ForgotPasswordRequest(BaseModel):
    email: str

@router.get("/get-admins/")
def get_admins(db: Session = Depends(get_db)):
    return db.query(Admin).all()

# Create a new admin (password will be stored as plain text)
@router.post("/admins/")
def create_admin(email: str, password: str, db: Session = Depends(get_db)):
    admin = Admin(
        email=email, 
        password=password,  # Store the plain text password
        created_on=datetime.now(india_timezone), 
        modified_on=datetime.now(india_timezone), 
        is_deleted=False
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin

# Admin login (plain text password comparison)
@router.post("/admin/login")
def admin_login(request: LoginRequest, db: Session = Depends(get_db)):
    # Fetch the admin from the database
    admin = db.query(Admin).filter(Admin.email == request.email).first()

    # If the admin doesn't exist, return an error
    if not admin:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Compare the plain text password directly
    if request.password != admin.password:  # Direct comparison for plain text
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # If the comparison is successful, proceed with the login
    return {"message": "Login Successful"}

# Forgot Password route (just a placeholder for now)
@router.post("/admin/forgot-password")
def forgot_password(request: ForgotPasswordRequest, db: Session = Depends(get_db)):
    # Check if the email exists in the database
    admin = db.query(Admin).filter(Admin.email == request.email).first()

    if not admin:
        raise HTTPException(status_code=404, detail="Email not found")

    # Here you should implement functionality for generating a password reset link
    # and sending it via email (this can be done using a service like SMTP).
    # For now, we'll return a success message.
    
    return {"message": "Password reset instructions have been sent to your email."}
