"""followers

Revision ID: 24e0551286da
Revises: 15bca622007e
Create Date: 2023-03-03 09:20:16.793302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24e0551286da'
down_revision = '15bca622007e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
