"""followers

Revision ID: 3a61f50e4599
Revises: d74b6cc6e67c
Create Date: 2022-07-14 16:34:14.407224

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "3a61f50e4599"
down_revision = "d74b6cc6e67c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "followers",
        sa.Column("follower_id", sa.Integer(), nullable=True),
        sa.Column("followed_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["followed_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["follower_id"],
            ["user.id"],
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("followers")
    # ### end Alembic commands ###