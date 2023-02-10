from flask import request, Blueprint
from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services.package_service import get_latest_releases, get_package_count, get_release_count
from pypi_org.services.user_service import get_user_count
import pypi_org.infrastructure.cookie_auth as cookie_auth

blueprint = Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    return {
        'releases': get_latest_releases(),
        'package_count': get_package_count(),
        'release_count': get_release_count(),
        'user_count': get_user_count(),
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }
