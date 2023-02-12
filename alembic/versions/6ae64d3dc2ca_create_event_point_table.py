"""create event point table

Revision ID: 6ae64d3dc2ca
Revises: 9f192de1bfd6
Create Date: 2023-02-08 12:57:40.680105

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date
import random

# revision identifiers, used by Alembic.
revision = '6ae64d3dc2ca'
down_revision = '9f192de1bfd6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    
    op.create_table(
        "event_points",
        sa.Column("name", sa.String),
        sa.Column("user_id", sa.String, ForeignKey("user_info.user_id"), primary_key = True, unique = True),
        sa.Column("team_buying", sa.Integer, nullable = False),
        sa.Column("working_report", sa.Integer, nullable = False),
        sa.Column("docs_apply", sa.Integer, nullable = False)
        # PrimaryKeyConstraint("user_id", name = "Primary key of event points")
    )
    
    event_table = table('event_points',
        column('name', String),
        column('user_id', String),
        column('team_buying', Integer),
        column('working_report', Integer),
        column('docs_apply', Integer),
    )

    op.bulk_insert(event_table,
    [
        {'name':'HI', 'user_id': 'HI', 'team_buying': 0, 'working_report': 0,'docs_apply': 273},
        {'name':'紘霈', 'user_id': '682545840291577856', 'team_buying': 0, 'working_report': 0,'docs_apply': 300},

    ],
        multiinsert=False
    )

    user_table = table('user_info',
        column('name', String),
        column('user_id', String),
        column('points', Integer),
    )

    insert_users = []
    insert_events = []
    for i in range(100):
        team_buying_point = random.randint(0, 3000)
        working_report_point = random.randint(0, 3000)
        docs_apply_point = random.randint(0, 3000)
        insert_users.append({'name' : f"user{i}", 'user_id': f"user{i}_testID", 'points' : team_buying_point + working_report_point + docs_apply_point})
        insert_events.append({'name' : f"user{i}", 'user_id': f"user{i}_testID", 'team_buying' : team_buying_point, 'working_report': working_report_point, 'docs_apply': docs_apply_point})
        
    op.bulk_insert(user_table, insert_users, multiinsert = False)
    op.bulk_insert(event_table, insert_events, multiinsert = False)

def downgrade() -> None:
    op.drop_table('event_points')
    op.drop_table('user_info')
