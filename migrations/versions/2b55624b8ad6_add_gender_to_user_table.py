"""add gender to user table

Revision ID: 2b55624b8ad6
Revises: 45422a980a9a
Create Date: 2026-03-10 11:58:38.561175

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b55624b8ad6'
down_revision: Union[str, Sequence[str], None] = '45422a980a9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("gender", sa.Integer, nullable=False)
    )


def downgrade() -> None:
    op.drop_column("users", "gender")