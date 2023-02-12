"""Add new column email to user info

Revision ID: 07d09166de45
Revises: 6ae64d3dc2ca
Create Date: 2023-02-09 12:58:43.024941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07d09166de45'
down_revision = '6ae64d3dc2ca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("user_info", sa.Column("email", sa.VARCHAR, nullable = True))


def downgrade() -> None:
    op.drop_column("user_info", "email")