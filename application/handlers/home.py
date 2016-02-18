# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import render_template

bp = Blueprint('front', __name__, template_folder='templates')

@bp.route('/')
def main():
    return render_template("index.html")