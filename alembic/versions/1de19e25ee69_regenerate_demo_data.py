"""regenerate demo data

Revision ID: 1de19e25ee69
Revises: 2b23c75174bf
Create Date: 2023-02-10 01:06:16.630994

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import String, Integer, BIGINT
from sqlalchemy.sql import table, column
import random

# revision identifiers, used by Alembic.
revision = '1de19e25ee69'
down_revision = '2b23c75174bf'
branch_labels = None
depends_on = None


def upgrade() -> None:

    event_table = table('event_points',
        column('name', String),
        column('user_id', BIGINT),
        column('team_buying', Integer),
        column('working_report', Integer),
        column('docs_apply', Integer),
    )

    user_table = table('user_info',
        column('name', String),
        column('user_id', BIGINT),
        column('points', Integer),
    )

    insert_users = []
    insert_events = []
    for i in range(100):
        team_buying_point = random.randint(0, 3000)
        working_report_point = random.randint(0, 3000)
        docs_apply_point = random.randint(0, 3000)
        insert_users.append({'name' : f"user{i}", 'user_id': i, 'points' : team_buying_point + working_report_point + docs_apply_point})
        insert_events.append({'name' : f"user{i}", 'user_id': i, 'team_buying' : team_buying_point, 'working_report': working_report_point, 'docs_apply': docs_apply_point})
        
    op.bulk_insert(user_table, insert_users, multiinsert = False)
    op.bulk_insert(event_table, insert_events, multiinsert = False)


def downgrade() -> None:
    pass
