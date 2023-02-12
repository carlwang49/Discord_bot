"""add emoji table

Revision ID: 9f192de1bfd6
Revises: dc22497f2445
Create Date: 2023-02-07 22:53:13.000583

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

# revision identifiers, used by Alembic.
revision = '9f192de1bfd6'
down_revision = 'dc22497f2445'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "emoji_info",
        sa.Column("emoji_eng", sa.String, nullable = False, primary_key = True, unique = True),
        sa.Column("emoji_id", sa.String, nullable = False,),
        sa.Column("emoji_name", sa.String, nullable = False),
    )
    
    emoji_table = table('emoji_info',
        column('emoji_eng', String),
        column('emoji_id', String),
        column('emoji_name', String)
    )

    op.bulk_insert(emoji_table,
    [
        {'emoji_eng':'zero_', 'emoji_id': '1072502300947513415', 'emoji_name': '0'},
        {'emoji_eng':'one_', 'emoji_id': '1072502296560291980', 'emoji_name': '1'},
        {'emoji_eng':'two_', 'emoji_id': '1072502292349198346', 'emoji_name': '2'},
        {'emoji_eng':'three_', 'emoji_id': '1072502286942732308', 'emoji_name': '3'},
        {'emoji_eng':'four_', 'emoji_id': '1072502282417082418', 'emoji_name': '4'},
        {'emoji_eng':'five_', 'emoji_id': '1072502278352801793', 'emoji_name': '5'},
        {'emoji_eng':'six_', 'emoji_id': '1072502273994924072', 'emoji_name': '6'},
        {'emoji_eng':'seven_', 'emoji_id': '1072502271021158541', 'emoji_name': '7'},
        {'emoji_eng':'eight_', 'emoji_id': '1072502266604552262', 'emoji_name': '8'},
        {'emoji_eng':'nine_', 'emoji_id': '1072502261625933887', 'emoji_name': '9'},
    ],
        multiinsert=False
    )

def downgrade() -> None:
    op.drop_table("emoji_info")