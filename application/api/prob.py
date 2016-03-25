# -*- coding:utf-8 -*-

from flask import jsonify, request, abort, json
from sqlalchemy import desc
from .base import ApiBlueprint
from application.models import db, PB
from .utils import row2dict
from .sql import sql_prob_get_by_id

api = ApiBlueprint('prob')

@api.route('')
def index():
    data = PB.query.all()
    return jsonify(data = [row2dict(row) for row in data])

# Get probs by modell and KDNR
@api.route('/mk/<modell>/<kdnr>')
def probs_mk(modell=None, kdnr=None):
    data = PB.query.filter(PB.MDL_TYP == modell ,PB.KDNR == kdnr).order_by(desc(PB.INS_D)).all()
    return jsonify(data = [row2dict(row) for row in data])

# Get one prob by id
@api.route('/<int:id>')
def prob_get_by_id(id):
    # data = PB.query.get(id)
    data = db.session.execute(sql_prob_get_by_id, {'id': id}).first()
    # print(data)
    # print(data['id'])
    # print(type(data))
    # print(dict(data.items()))
    return jsonify(data= dict(data.items()))


@api.route('/add', methods=['POST'])
def add():
    # print('GET POST FROM CLIENT')
    # print(request.form)
    # print(request.json)
    plv = request.form.get('plv', None)
    pbc = request.form.get('text', None)
    prob = PB()
    prob.MDL_TYP = '34'
    prob.KDNR = '2332'
    prob.PBC = pbc
    prob.PBD = 'ddd'
    prob.PBE = 'EEE'
    prob.PLV = plv
    with db.auto_commit():
    	db.session.add(prob)

    data = PB.query.all()
    return jsonify(data = [row2dict(row) for row in data])