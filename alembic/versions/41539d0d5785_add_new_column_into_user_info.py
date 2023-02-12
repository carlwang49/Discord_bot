"""add new column into user_info

Revision ID: 41539d0d5785
Revises: be7b3627f5fa
Create Date: 2023-02-11 01:52:17.571290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41539d0d5785'
down_revision = 'be7b3627f5fa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('user_info', sa.Column('title', sa.VARCHAR))
    op.add_column('user_info', sa.Column('department', sa.VARCHAR))

def downgrade() -> None:
    op.drop_column("user_info", 'title')
    op.drop_column("user_info", 'department')