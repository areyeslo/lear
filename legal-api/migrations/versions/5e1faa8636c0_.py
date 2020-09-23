"""empty message

Revision ID: 5e1faa8636c0
Revises: 2e986c1d4de6
Create Date: 2020-09-21 17:13:36.642571

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5e1faa8636c0'
down_revision = '2e986c1d4de6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('addresses_office_id_fkey', 'addresses', type_='foreignkey')
    op.create_foreign_key('addresses_office_id_fkey_new', 'addresses', 'offices', ['office_id'], ['id'],
                          ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('addresses_office_id_fkey_new', 'addresses', type_='foreignkey')
    op.create_foreign_key('addresses_office_id_fk', 'addresses', 'offices', ['office_id'], ['id'])
    # ### end Alembic commands ###