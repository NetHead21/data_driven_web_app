from datetime import datetime
import sqlalchemy as sa
from pypi_org.data.modelbase import SqlAlchemyBase

class License(SqlAlchemyBase):
    __tablename__ = 'linceses'

    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.now, index=True)
    description = sa.Column(sa.String)
    