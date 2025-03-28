"""added new columns v2

Revision ID: c21fca354d8e
Revises: a6e48e9e654a
Create Date: 2025-02-15 14:10:08.178789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c21fca354d8e'
down_revision = 'a6e48e9e654a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('firm', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sgst', sa.Numeric(), nullable=False))
        batch_op.add_column(sa.Column('igst', sa.Numeric(), nullable=False))
        batch_op.add_column(sa.Column('custom_fields', sa.LargeBinary(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('firm', schema=None) as batch_op:
        batch_op.drop_column('custom_fields')
        batch_op.drop_column('igst')
        batch_op.drop_column('sgst')

    # ### end Alembic commands ###
