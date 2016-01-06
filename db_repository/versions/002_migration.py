from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
lecture = Table('lecture', post_meta,
    Column('lecture_id', Integer, primary_key=True, nullable=False),
    Column('lecture_name', String(length=64)),
    Column('order', Integer),
    Column('lecture_abstract', String(length=600)),
    Column('course_id', Integer),
    Column('video_url', String(length=600)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['lecture'].columns['order'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['lecture'].columns['order'].drop()
