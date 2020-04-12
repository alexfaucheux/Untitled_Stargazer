"""empty message

Revision ID: cac314856c95
Revises: 
Create Date: 2020-04-12 10:36:33.131637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cac314856c95'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_name', sa.String(length=64), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('image_name'),
    sa.UniqueConstraint('image_url')
    )
    op.create_table('object_of_interest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('date_stored', sa.DateTime(), nullable=True),
    sa.Column('vis_start', sa.DateTime(), nullable=True),
    sa.Column('vis_end', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_object_of_interest_date_stored'), 'object_of_interest', ['date_stored'], unique=False)
    op.create_index(op.f('ix_object_of_interest_vis_end'), 'object_of_interest', ['vis_end'], unique=False)
    op.create_index(op.f('ix_object_of_interest_vis_start'), 'object_of_interest', ['vis_start'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=True),
    sa.Column('fname', sa.String(length=64), nullable=True),
    sa.Column('lname', sa.String(length=64), nullable=True),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_fname'), 'user', ['fname'], unique=False)
    op.create_index(op.f('ix_user_lname'), 'user', ['lname'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('weather',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_stored', sa.DateTime(), nullable=True),
    sa.Column('sunset', sa.DateTime(), nullable=True),
    sa.Column('sunrise', sa.DateTime(), nullable=True),
    sa.Column('high', sa.FLOAT(), nullable=True),
    sa.Column('low', sa.FLOAT(), nullable=True),
    sa.Column('m_phase', sa.String(), nullable=True),
    sa.Column('clouds', sa.FLOAT(), nullable=True),
    sa.Column('wind', sa.FLOAT(), nullable=True),
    sa.Column('wind_dir', sa.FLOAT(), nullable=True),
    sa.Column('vis', sa.FLOAT(), nullable=True),
    sa.Column('current', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_weather_date_stored'), 'weather', ['date_stored'], unique=False)
    op.create_table('user_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('image_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['image_id'], ['image.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_image_image_id'), 'user_image', ['image_id'], unique=False)
    op.create_index(op.f('ix_user_image_user_id'), 'user_image', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_image_user_id'), table_name='user_image')
    op.drop_index(op.f('ix_user_image_image_id'), table_name='user_image')
    op.drop_table('user_image')
    op.drop_index(op.f('ix_weather_date_stored'), table_name='weather')
    op.drop_table('weather')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_lname'), table_name='user')
    op.drop_index(op.f('ix_user_fname'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_object_of_interest_vis_start'), table_name='object_of_interest')
    op.drop_index(op.f('ix_object_of_interest_vis_end'), table_name='object_of_interest')
    op.drop_index(op.f('ix_object_of_interest_date_stored'), table_name='object_of_interest')
    op.drop_table('object_of_interest')
    op.drop_table('image')
    # ### end Alembic commands ###
