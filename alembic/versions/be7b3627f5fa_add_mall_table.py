"""add MALL table

Revision ID: be7b3627f5fa
Revises: 20a8e22776b7
Create Date: 2023-02-11 01:28:27.965592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be7b3627f5fa'
down_revision = '20a8e22776b7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mall',
    sa.Column('commodity', sa.VARCHAR(), nullable=False),
    sa.Column('points', sa.VARCHAR(), nullable=False),
    sa.Column('amount', sa.VARCHAR(), nullable=False),
    sa.Column('image_url', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('commodity')
    )
    
    # op.alter_column('emoji_info', 'emoji_name',
    #            existing_type=sa.VARCHAR(),
    #            nullable=True)
    # op.create_unique_constraint(None, 'emoji_info', ['emoji_eng'])
    # op.create_unique_constraint(None, 'event_points', ['user_id'])
    # op.alter_column('menu', 'number',
    #            existing_type=sa.INTEGER(),
    #            server_default=None,
    #            existing_nullable=False,
    #            autoincrement=True)
    # op.create_unique_constraint(None, 'menu', ['number'])
    # op.create_unique_constraint(None, 'user_info', ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_constraint(None, 'user_info', type_='unique')
    # op.drop_constraint(None, 'menu', type_='unique')
    # op.alter_column('menu', 'number',
    #            existing_type=sa.INTEGER(),
    #            server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1),
    #            existing_nullable=False,
    #            autoincrement=True)
    # op.drop_constraint(None, 'event_points', type_='unique')
    # op.drop_constraint(None, 'emoji_info', type_='unique')
    # op.alter_column('emoji_info', 'emoji_name',
    #            existing_type=sa.VARCHAR(),
            #    nullable=False)
    op.drop_table('mall')
    # ### end Alembic commands ###
