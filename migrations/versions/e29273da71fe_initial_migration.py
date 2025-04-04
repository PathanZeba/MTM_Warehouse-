"""initial migration

Revision ID: e29273da71fe
Revises: 
Create Date: 2025-03-25 00:31:52.561736

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = 'e29273da71fe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Job_Progress',
    sa.Column('Job_Progress_Id', sa.Integer(), nullable=False),
    sa.Column('Progress_Status', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('Job_Progress_Id'),
    schema='dbo'
    )
    op.create_table('Users',
    sa.Column('Id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Username', sa.String(length=255), nullable=False),
    sa.Column('NormalizedUsername', sa.String(length=255), nullable=True),
    sa.Column('Email', sa.String(length=255), nullable=True),
    sa.Column('NormalizedEmail', sa.String(length=255), nullable=True),
    sa.Column('EmailConfirmed', sa.Boolean(), nullable=False),
    sa.Column('PasswordHash', sa.String(length=512), nullable=False),
    sa.Column('SecurityStamp', sa.String(length=255), nullable=True),
    sa.Column('ConcurrencyStamp', sa.String(length=255), nullable=True),
    sa.Column('PhoneNumber', sa.String(length=20), nullable=True),
    sa.Column('PhoneNumberConfirmed', sa.Boolean(), nullable=False),
    sa.Column('TwoFactorEnabled', sa.Boolean(), nullable=False),
    sa.Column('LockoutEnd', sa.DateTime(), nullable=True),
    sa.Column('LockoutEnabled', sa.Boolean(), nullable=False),
    sa.Column('AccessFailedCount', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('Id'),
    sa.UniqueConstraint('Email'),
    sa.UniqueConstraint('NormalizedEmail'),
    sa.UniqueConstraint('NormalizedUsername'),
    sa.UniqueConstraint('Username'),
    schema='dbo'
    )
    op.create_table('Warehouse_Info',
    sa.Column('Warehouse_Info_Id', sa.Integer(), nullable=False),
    sa.Column('W_Name', sa.String(), nullable=False),
    sa.Column('W_Location', sa.String(), nullable=False),
    sa.Column('W_Pincode', sa.String(), nullable=False),
    sa.Column('W_Total_capacity', sa.Float(), nullable=False),
    sa.Column('W_Space_Available', sa.Float(), nullable=True),
    sa.Column('W_Percent_Full', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('Warehouse_Info_Id'),
    schema='dbo'
    )
    op.create_table('Approval_Jobs',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Transport_Item', sa.String(length=255), nullable=False),
    sa.Column('Item_Space', sa.String(length=255), nullable=False),
    sa.Column('From_Warehouse', sa.String(length=255), nullable=False),
    sa.Column('To_Warehouse', sa.String(length=255), nullable=False),
    sa.Column('Item_Quantity', sa.String(length=255), nullable=False),
    sa.Column('Approval_Status', sa.String(length=255), nullable=False),
    sa.Column('Job_Progress_Id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Job_Progress_Id'], ['dbo.Job_Progress.Job_Progress_Id'], ),
    sa.PrimaryKeyConstraint('Id'),
    schema='dbo'
    )
    op.create_table('Emp_Data',
    sa.Column('Emp_Data_Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=100), nullable=False),
    sa.Column('Position', sa.String(length=100), nullable=False),
    sa.Column('Salary', sa.Float(), nullable=False),
    sa.Column('Warehouse_Info_Id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Warehouse_Info_Id'], ['dbo.Warehouse_Info.Warehouse_Info_Id'], ),
    sa.PrimaryKeyConstraint('Emp_Data_Id'),
    schema='dbo'
    )
    op.create_table('Login_Emp',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=30), nullable=True),
    sa.Column('Email', sa.String(length=255), nullable=True),
    sa.Column('Role', sa.String(length=255), nullable=True),
    sa.Column('Username', sa.String(length=255), nullable=True),
    sa.Column('Password_Hash', sa.String(length=255), nullable=False),
    sa.Column('Warehouse_Info_Id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Warehouse_Info_Id'], ['dbo.Warehouse_Info.Warehouse_Info_Id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('Id'),
    sa.UniqueConstraint('Email'),
    sa.UniqueConstraint('Username'),
    schema='dbo'
    )
    op.create_table('Warehouse_Items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('warehouse_info_id', sa.Integer(), nullable=True),
    sa.Column('Item_Name', sa.String(), nullable=False),
    sa.Column('Item_Unit_Quant', sa.Float(), nullable=False),
    sa.Column('Item_Capacity_Quant', sa.Float(), nullable=False),
    sa.Column('Item_Space_Acquired', sa.Float(), nullable=True),
    sa.Column('Item_Price_Per_Unit', sa.Float(), nullable=False),
    sa.Column('Item_Total_Cost', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['warehouse_info_id'], ['dbo.Warehouse_Info.Warehouse_Info_Id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='dbo'
    )
    op.create_table('Approvals',
    sa.Column('Id', sa.String(length=255), nullable=False),
    sa.Column('Applicant_Id', sa.String(length=255), nullable=False),
    sa.Column('Applicant_Name', sa.String(length=255), nullable=False),
    sa.Column('Message', sa.String(length=1000), nullable=False),
    sa.Column('Approval_job', sa.String(length=255), nullable=False),
    sa.Column('Login_Emp_Id', sa.Integer(), nullable=True),
    sa.Column('Approval_Jobs_Id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Approval_Jobs_Id'], ['dbo.Approval_Jobs.Id'], ),
    sa.ForeignKeyConstraint(['Login_Emp_Id'], ['dbo.Login_Emp.Id'], ),
    sa.PrimaryKeyConstraint('Id'),
    schema='dbo'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Approvals', schema='dbo')
    op.drop_table('Warehouse_Items', schema='dbo')
    op.drop_table('Login_Emp', schema='dbo')
    op.drop_table('Emp_Data', schema='dbo')
    op.drop_table('Approval_Jobs', schema='dbo')
    op.drop_table('Warehouse_Info', schema='dbo')
    op.drop_table('Users', schema='dbo')
    op.drop_table('Job_Progress', schema='dbo')
    # ### end Alembic commands ###
