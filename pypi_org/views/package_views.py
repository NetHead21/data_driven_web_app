from flask import request, Blueprint, abort
from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services.package_service import get_latest_releases, get_package_by_id
import pypi_org.infrastructure.cookie_auth as cookie_auth

blueprint = Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
@response(template_file='packages/details.html')
def package_details(package_name: str):
    if not package_name:
        return abort(status=404)

    package = get_package_by_id(package_name.strip().lower())
    if not package:
        return abort(status=404)

    latest_version = "0.0.0"
    latest_release = None
    is_latest = True

    if package.releases:
        latest_release = package.releases[0]
        latest_version = latest_release.version_text

    return {
        'package': package,
        'latest_version': latest_version,
        'latest_release': latest_release,
        'release_version': latest_release,
        'is_latest': is_latest,
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }


@blueprint.route('/<int:rank>')
def popular(rank: int):
    return f"The details for the {rank} most popular package."
