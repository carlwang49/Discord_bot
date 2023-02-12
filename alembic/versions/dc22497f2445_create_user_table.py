"""create user table

Revision ID: dc22497f2445
Revises: 
Create Date: 2023-02-05 15:19:44.060296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc22497f2445'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user_info",
        sa.Column("name", sa.String, nullable = False),
        sa.Column("user_id", sa.String, nullable = False, primary_key = True),
        sa.Column("points", sa.Integer, nullable = False),
    )


def downgrade() -> None:
    op.drop_table("user_info")
