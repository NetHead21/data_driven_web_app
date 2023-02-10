import os
import sys
import flask
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)
import pypi_org.data.db_session as db_session

app = flask.Flask(__name__)

app.config["SECRET_KEY"] = "@V5Zfaf%K&I^2Z2w9cT0drb62"

def main():
    register_blueprint()
    setup_db()
    app.run(debug=True)


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'pypi.sqlite'
    )

    db_session.global_init(db_file)


def register_blueprint():
    from pypi_org.views import home_views
    from pypi_org.views import package_views
    from pypi_org.views import cms_views
    from pypi_org.views import account_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(cms_views.blueprint)
    app.register_blueprint(account_views.blueprint)


if __name__ == '__main__':
    main()
