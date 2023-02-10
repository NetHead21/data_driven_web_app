import os
import sys
# Make it run more easily outside of PyCharm
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..")))

from pypi_org.data.releases import Release
from pypi_org.data.package import Package
import pypi_org.data.db_session as db_session




print(sys.path)

def main():
    init_db()
    while True:
        insert_a_package()


def init_db():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..', 'db', 'pypi.sqlite')
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)


def insert_a_package():
    p = Package()
    p.id = input("Package id / name: ").strip().lower()

    p.summary = input("Package summary / name: ").strip()
    p.author_name = input("Package author name: ").strip()
    p.license = input("License: ").strip()

    # author_name = sa.Column(sa.String)
    # license = sa.Column(sa.String, index=True)

    print("Release 1")
    r = Release()
    r.major_ver = int(input("Major Version: "))
    r.minor_ver = int(input("Minor Version: "))
    r.build_ver = int(input("Build Version: "))
    r.size = int(input("Size in bytes: "))
    p.releases.append(r)

    print("Release 2")
    r = Release()
    r.major_ver = int(input("Major Version: "))
    r.minor_ver = int(input("Minor Version: "))
    r.build_ver = int(input("Build Version: "))
    r.size = int(input("Size in bytes: "))
    p.releases.append(r)


    session = db_session.create_session()
    session.add(p)
    session.commit()


if __name__ == '__main__':
    main()
