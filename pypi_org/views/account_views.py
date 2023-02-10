from flask import redirect, url_for, request, flash, Blueprint

from pypi_org.infrastructure.view_modifiers import response
import pypi_org.services.user_service as user_service
import pypi_org.infrastructure.cookie_auth as cookie_auth
import pypi_org.infrastructure.request_dict as request_dict
from pypi_org.viewmodels.account.index_view_model import IndexViewModel
from pypi_org.viewmodels.account.register_view_model import RegisterViewModel

blueprint = Blueprint('account', __name__, template_folder='templates')


# INDEX #########################################################################
@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    vm = IndexViewModel()
    if not vm.user:
        return redirect('/account/login')

    return vm.to_dict()


# REGISTER ######################################################################
@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    vm = RegisterViewModel()
    return vm.to_dict()


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    vm = RegisterViewModel()
    vm.validate()

    if vm.error:
        flash(f"{vm.error[0]}", category=f"{vm.error[1]}")
        return vm.to_dict()
    
    # TODO: Create the user
    user = user_service.create_user(vm.name, vm.email, vm.password)

    if not user:
        flash(f"{vm.error[0]}", category=f"{vm.error[1]}")
        return vm.to_dict()

    flash("Register Successfully.", category="success")

    # TODO: Log in browser as a session
    resp = redirect('/account')
    cookie_auth.set_auth(resp, user.id)
    
    return resp


# LOGIN ########################################################################
@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    return {}


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    data = request_dict.create()
    email = data.email.strip()
    password = data.password.strip()

    if not email or not password:
        flash("Some require field are missing.", category="danger")
        return {
            'email': email,
            'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
        }


    # TODO: Validate the user
    user = user_service.login_user(email, password)

    if not user:
        flash("User does not exists or Invalid Password.", category="danger")
        return {
            'email': email,
            'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
        }
    flash("Login Successfully.", category="success")

    # TODO: Log in browser as a session
    resp = redirect('/account')
    cookie_auth.set_auth(resp, user.id)

    return resp


# LOGOUT ######################################################################
@blueprint.route('/account/logout')
def logout():
    resp = redirect('/')
    cookie_auth.logout(resp)

    return resp
