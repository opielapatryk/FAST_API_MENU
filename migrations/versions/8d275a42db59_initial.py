"""Initial

Revision ID: 8d275a42db59
Revises: 
Create Date: 2024-04-12 12:11:26.760477

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d275a42db59'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dishes', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('dishes', sa.Column('name', sa.String(), nullable=False))
    op.add_column('dishes', sa.Column('description', sa.String(), nullable=False))
    op.add_column('dishes', sa.Column('price', sa.Float(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dishes', 'price')
    op.drop_column('dishes', 'description')
    op.drop_column('dishes', 'name')
    op.drop_column('dishes', 'id')
    # ### end Alembic commands ###
