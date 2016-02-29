# -*- coding:utf-8 -*-

row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
