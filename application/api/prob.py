# -*- coding:utf-8 -*-

from flask import jsonify
from .base import ApiBlueprint
from application.models import db, PB
from .utils import row2dict

api = ApiBlueprint('prob')

@api.route('')
def index():
    data = PB.query.all()
    return jsonify(data = [row2dict(row) for row in data])

@api.route('/add', methods=['GET'])
def add():
    prob = PB()
    prob.MDL_TYP = '34'
    prob.KDNR = '2332'
    prob.PBC = 'aaa'
    prob.PBD = 'ddd'
    prob.PBE = 'EEE'
    with db.auto_commit():
    	db.session.add(prob)
    return jsonify(data = prob.PBC)