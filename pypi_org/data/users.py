from datetime import datetime
import sqlalchemy as sa
from pypi_org.data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, unique=True, nullable=True, index=True)
    hashed_password = sa.Column(sa.String, nullable=True, index=True)
    created_dated = sa.Column(sa.DateTime, nullable=True, index=True)
    profile_image_url = sa.Column(sa.String)
    last_login = sa.Column(sa.DateTime, default=datetime.now, index=True)
