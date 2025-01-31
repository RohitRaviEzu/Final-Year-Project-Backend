from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.database import Base
from datetime import datetime, timezone

class Admin(Base):
    __tablename__ = "admin_table"

    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_on = Column(DateTime, default=datetime.now(timezone.utc))  # Timezone-aware UTC datetime
    modified_on = Column(DateTime, onupdate=datetime.now(timezone.utc))  # Timezone-aware UTC datetime
    is_deleted = Column(Boolean, default=False)


