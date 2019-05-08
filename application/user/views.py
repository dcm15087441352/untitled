from flask import render_template
from ..extensions import flask_db
from ..models import User

from . import bp_user


@bp_user.route('/list_users')
def list_users():
    users = User.select()
    return render_template('user/list_users.html', users=users)

