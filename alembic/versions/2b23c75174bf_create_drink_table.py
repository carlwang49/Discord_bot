"""Create drink table

Revision ID: 2b23c75174bf
Revises: 07d09166de45
Create Date: 2023-02-09 22:15:42.941431

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '2b23c75174bf'
down_revision = '07d09166de45'
branch_labels = None
depends_on = None


def upgrade() -> None:


    op.create_table(
        "menu",
        sa.Column("number", sa.Integer,sa.Identity() , nullable = False),
        sa.Column("brand", sa.String, nullable = False),
        sa.Column("item", sa.String, nullable = False),
        sa.Column("price_small", sa.Integer, nullable = False),
        sa.Column("price_large", sa.Integer, nullable = False)
    )

    menu_table = table('menu',
        sa.Column('brand', sa.String),
        sa.Column('item', sa.String),
        sa.Column('price_small', sa.Integer),
        sa.Column('price_large', sa.Integer),
    )

    op.bulk_insert(menu_table,
        [
            {'brand': '五十嵐', 'item': '茉莉綠茶',
            'price_small': 25, 'price_large': 30},
            {'brand': '五十嵐', 'item': '阿薩姆紅茶',
            'price_small': 25, 'price_large': 30},
            {'brand': '五十嵐', 'item': '四季春青茶',
            'price_small': 25, 'price_large': 30},
            {'brand': '五十嵐', 'item': '黃金烏龍',
            'price_small': 25, 'price_large': 30},
            {'brand': '五十嵐', 'item': '波霸紅',
            'price_small': 30, 'price_large': 40},
            {'brand': '五十嵐', 'item': '波霸綠',
            'price_small': 30, 'price_large': 40},
            {'brand': '五十嵐', 'item': '燕麥紅',
            'price_small': 30, 'price_large': 40},
            {'brand': '五十嵐', 'item': '燕麥綠',
            'price_small': 30, 'price_large': 40},
            {'brand': '五十嵐', 'item': '燕麥青',
            'price_small': 30, 'price_large': 40},
            {'brand': '五十嵐', 'item': '微檸檬紅',
            'price_small': 30, 'price_large': 40},
            {'brand': '五十嵐', 'item': '微檸檬青',
            'price_small': 30, 'price_large': 40},
            {'brand': '五十嵐', 'item': '檸檬綠',
            'price_small': 35, 'price_large': 50},
            {'brand': '五十嵐', 'item': '檸檬青',
            'price_small': 30, 'price_large': 50},
            {'brand': '五十嵐', 'item': '梅の綠',
            'price_small': 35, 'price_large': 50},
            {'brand': '五十嵐', 'item': '8冰綠',
            'price_small': 35, 'price_large': 50},
            {'brand': '五十嵐', 'item': '情人茶',
            'price_small': 35, 'price_large': 50},
            {'brand': '五十嵐', 'item': '多多綠',
            'price_small': 35, 'price_large': 50},
            {'brand': '五十嵐', 'item': '冰淇淋紅茶',
            'price_small': 35, 'price_large': 50},
            {'brand': '五十嵐', 'item': '旺來紅',
            'price_small': 35, 'price_large': 50},
            {'brand': '五十嵐', 'item': '旺來青',
            'price_small': 35, 'price_large': 50},
            {'brand': '五十嵐', 'item': '蜂蜜紅',
            'price_small': 35, 'price_large': 50},
            {'brand': '五十嵐', 'item': '蜂蜜綠',
            'price_small': 35, 'price_large': 50},
            {'brand': '五十嵐', 'item': '鮮柚綠',
            'price_small': 45, 'price_large': 60},
            {'brand': '五十嵐', 'item': '奶茶',
            'price_small': 35, 'price_large': 50},
            {'brand': '五十嵐', 'item': '奶綠',
            'price_small': 35, 'price_large': 50}
        ],
        multiinsert=False
    )


def downgrade() -> None:
    op.drop_table('menu')