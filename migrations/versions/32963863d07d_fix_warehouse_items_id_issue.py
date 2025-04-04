"""Fix warehouse_items_id issue

Revision ID: 32963863d07d
Revises: e29273da71fe
Create Date: 2025-03-25 00:39:19.521731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32963863d07d'
down_revision = 'e29273da71fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Approval_Jobs', schema=None) as batch_op:
        batch_op.drop_constraint('FK__Approval___Job_P__4316F928', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Job_Progress', ['Job_Progress_Id'], ['Job_Progress_Id'], referent_schema='dbo')

    with op.batch_alter_table('Approvals', schema=None) as batch_op:
        batch_op.drop_constraint('FK__Approvals__Appro__5070F446', type_='foreignkey')
        batch_op.drop_constraint('FK__Approvals__Login__5165187F', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Approval_Jobs', ['Approval_Jobs_Id'], ['Id'], referent_schema='dbo')
        batch_op.create_foreign_key(None, 'Login_Emp', ['Login_Emp_Id'], ['Id'], referent_schema='dbo')

    with op.batch_alter_table('Emp_Data', schema=None) as batch_op:
        batch_op.drop_constraint('FK__Emp_Data__Wareho__45F365D3', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Warehouse_Info', ['Warehouse_Info_Id'], ['Warehouse_Info_Id'], referent_schema='dbo')

    with op.batch_alter_table('Login_Emp', schema=None) as batch_op:
        batch_op.drop_constraint('FK__Login_Emp__Wareh__4AB81AF0', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Warehouse_Info', ['Warehouse_Info_Id'], ['Warehouse_Info_Id'], referent_schema='dbo', ondelete='SET NULL')

    with op.batch_alter_table('Warehouse_Items', schema=None) as batch_op:
        batch_op.drop_constraint('FK__Warehouse__wareh__4D94879B', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Warehouse_Info', ['warehouse_info_id'], ['Warehouse_Info_Id'], referent_schema='dbo')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Warehouse_Items', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('FK__Warehouse__wareh__4D94879B', 'Warehouse_Info', ['warehouse_info_id'], ['Warehouse_Info_Id'])

    with op.batch_alter_table('Login_Emp', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('FK__Login_Emp__Wareh__4AB81AF0', 'Warehouse_Info', ['Warehouse_Info_Id'], ['Warehouse_Info_Id'], ondelete='SET NULL')

    with op.batch_alter_table('Emp_Data', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('FK__Emp_Data__Wareho__45F365D3', 'Warehouse_Info', ['Warehouse_Info_Id'], ['Warehouse_Info_Id'])

    with op.batch_alter_table('Approvals', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('FK__Approvals__Login__5165187F', 'Login_Emp', ['Login_Emp_Id'], ['Id'])
        batch_op.create_foreign_key('FK__Approvals__Appro__5070F446', 'Approval_Jobs', ['Approval_Jobs_Id'], ['Id'])

    with op.batch_alter_table('Approval_Jobs', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('FK__Approval___Job_P__4316F928', 'Job_Progress', ['Job_Progress_Id'], ['Job_Progress_Id'])

    # ### end Alembic commands ###
