import sqlalchemy as sa
import sqlalchemy.orm as orm
from pypi_org.data.modelbase import SqlAlchemyBase
from datetime import datetime
from pypi_org.data.releases import Release
from typing import List

class Package(SqlAlchemyBase):
    __tablename__ = 'packages'
    id = sa.Column(sa.String, primary_key=True)
    create_date = sa.Column(sa.DateTime, default=datetime.now, index=True)
    summary = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=True)

    home_page = sa.Column(sa.String)
    docs_url = sa.Column(sa.String)
    package_url = sa.Column(sa.String)

    author_name = sa.Column(sa.String)
    author_email = sa.Column(sa.String, index=True)

    license = sa.Column(sa.String, index=True)

    # maintainers
    # releases
    releases: List[Release] = orm.relation("Release", order_by=[
        Release.major_ver.desc(),
        Release.minor_ver.desc(),
        Release.build_ver.desc(),
    ], back_populates='package')

    def __repr__(self) -> str:
        return f'<Package {self.id}'