"""Fix warehouse_items_id column

Revision ID: b0ef7f3c4654
Revises: 32963863d07d
Create Date: 2025-03-25 00:41:50.065591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0ef7f3c4654'
down_revision = '32963863d07d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Approval_Jobs', schema=None) as batch_op:
        batch_op.drop_constraint('FK__Approval___Job_P__52593CB8', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Job_Progress', ['Job_Progress_Id'], ['Job_Progress_Id'], referent_schema='dbo')

    with op.batch_alter_table('Approvals', schema=None) as batch_op:
        batch_op.drop_constraint('FK__Approvals__Login__5441852A', type_='foreignkey')
        batch_op.drop_constraint('FK__Approvals__Appro__534D60F1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Approval_Jobs', ['Approval_Jobs_Id'], ['Id'], referent_schema='dbo')
        batch_op.create_foreign_key(None, 'Login_Emp', ['Login_Emp_Id'], ['Id'], referent_schema='dbo')

    with op.batch_alter_table('Emp_Data', schema=None) as batch_op:
        batch_op.drop_constraint('FK__Emp_Data__Wareho__5535A963', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Warehouse_Info', ['Warehouse_Info_Id'], ['Warehouse_Info_Id'], referent_schema='dbo')

    with op.batch_alter_table('Login_Emp', schema=None) as batch_op:
        batch_op.drop_constraint('FK__Login_Emp__Wareh__5629CD9C', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Warehouse_Info', ['Warehouse_Info_Id'], ['Warehouse_Info_Id'], referent_schema='dbo', ondelete='SET NULL')

    with op.batch_alter_table('Warehouse_Items', schema=None) as batch_op:
        batch_op.alter_column('warehouse_info_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_constraint('FK__Warehouse__wareh__571DF1D5', type_='foreignkey')
        batch_op.create_foreign_key(None, 'Warehouse_Info', ['warehouse_info_id'], ['Warehouse_Info_Id'], referent_schema='dbo')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Warehouse_Items', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('FK__Warehouse__wareh__571DF1D5', 'Warehouse_Info', ['warehouse_info_id'], ['Warehouse_Info_Id'])
        batch_op.alter_column('warehouse_info_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('Login_Emp', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('FK__Login_Emp__Wareh__5629CD9C', 'Warehouse_Info', ['Warehouse_Info_Id'], ['Warehouse_Info_Id'], ondelete='SET NULL')

    with op.batch_alter_table('Emp_Data', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('FK__Emp_Data__Wareho__5535A963', 'Warehouse_Info', ['Warehouse_Info_Id'], ['Warehouse_Info_Id'])

    with op.batch_alter_table('Approvals', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('FK__Approvals__Appro__534D60F1', 'Approval_Jobs', ['Approval_Jobs_Id'], ['Id'])
        batch_op.create_foreign_key('FK__Approvals__Login__5441852A', 'Login_Emp', ['Login_Emp_Id'], ['Id'])

    with op.batch_alter_table('Approval_Jobs', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('FK__Approval___Job_P__52593CB8', 'Job_Progress', ['Job_Progress_Id'], ['Job_Progress_Id'])

    # ### end Alembic commands ###
