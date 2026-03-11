import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class User(Base, table=True):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    
    name: Mapped[str] = mapped_column(
        String(55),
        unique=True,
        nullable=False,
        index=True
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    
    adress: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    
    has_advertisement_perm: Mapped[bool] = mapped_column(
        bool,
        nullable=False
    )
    
    gender: Mapped[int] = mapped_column(
        int,
        nullable=True
    )