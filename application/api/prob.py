# -*- coding:utf-8 -*-

from flask import jsonify
from .base import ApiBlueprint
from application.models import PB
from .utils import row2dict

api = ApiBlueprint('prob')

@api.route('')
def index():
    data = PB.query.all()
    return jsonify(data = [row2dict(row) for row in data])