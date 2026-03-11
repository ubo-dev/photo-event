"""add has_advertisement_perm

Revision ID: 45422a980a9a
Revises: 17d03cfe1c62
Create Date: 2026-03-10 11:39:35.505806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45422a980a9a'
down_revision: Union[str, Sequence[str], None] = '17d03cfe1c62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("has_advertisement_perm", sa.Boolean, nullable=False)
    )


def downgrade() -> None:
    op.drop_column("users", "has_advertisement_perm")
