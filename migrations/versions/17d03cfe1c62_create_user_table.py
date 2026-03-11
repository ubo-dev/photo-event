"""create user table

Revision ID: 17d03cfe1c62
Revises: 
Create Date: 2026-03-10 10:38:57.287851

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17d03cfe1c62'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.UUID, nullable=False),
        sa.Column("name", sa.String(55), nullable=False),
        sa.Column("email", sa.String(255), nullable=False, unique=True),
        sa.Column("hashed_password", sa.String(255), nullable=False),
        sa.Column("adress", sa.String(255), nullable=True)
    )


def downgrade() -> None:
    op.drop_table("users")
