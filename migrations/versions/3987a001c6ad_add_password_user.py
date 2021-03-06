"""Add password user

Revision ID: 3987a001c6ad
Revises: bcaf967c3a58
Create Date: 2021-10-25 20:28:57.798636

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '3987a001c6ad'
down_revision = 'bcaf967c3a58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###
