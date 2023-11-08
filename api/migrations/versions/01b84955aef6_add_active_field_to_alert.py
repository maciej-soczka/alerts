"""add active field to alert

Revision ID: 01b84955aef6
Revises: 816f69038051
Create Date: 2023-11-05 23:05:32.488843

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01b84955aef6'
down_revision: Union[str, None] = '816f69038051'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alert', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('alert', 'active')
    # ### end Alembic commands ###
