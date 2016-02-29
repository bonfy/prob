# -*- coding:utf-8 -*-

import time
import datetime
from sqlalchemy import Column
from sqlalchemy import String, Unicode, DateTime, Integer, NVARCHAR, TEXT, NCHAR, Numeric

from .base import Base

__all__ = ['PB', ]

class PB(Base):

    __tablename__ = 'PB'

    id = Column(Integer, primary_key=True)
    MDL_TYP = Column(NVARCHAR(10), nullable=False)
    KDNR = Column(NVARCHAR(10), nullable=False)
    PBC = Column(NVARCHAR(30), nullable=False)
    PBD = Column(NVARCHAR(80))
    PBE = Column(NVARCHAR(80))
    MARK = Column(TEXT)
    ND_TRAN = Column(NCHAR(1))
    QPZ = Column(Integer)
    FAP_KZ = Column(NCHAR(1))
    BA = Column(NCHAR(3))
    PB_STT = Column(Integer)
    FZG_VOL = Column(Integer)
    PRNR_STR = Column(NVARCHAR(100))
    KD_ORT = Column(NCHAR(3))
    LB_KZ = Column(NCHAR(1))
    PCD = Column(NCHAR(1))
    PS_KZ = Column(NCHAR(1))
    PB_EXT = Column(NVARCHAR(100))
    BEKANT_D = Column(DateTime, default=datetime.datetime.now)
    END_D = Column(DateTime)
    MOP1 = Column(Integer)
    MOP2 = Column(Integer)
    PLV = Column(NVARCHAR(100))
    USERNAME = Column(NVARCHAR(30))
    INS_D = Column(DateTime, default=datetime.datetime.now)
    UPD_D = Column(DateTime)
    TAXI = Column(NCHAR(1))

    def __repr__(self):
        return '<PB:%s>' % self.PBC

    def __str__(self):
        return self.PBC

    def keys(self):
        return (
            'id', 'PBC', 'PBD', 'PBE',
        )

class CA(Base):

    __tablename__ = 'CA'

    id = Column(Integer, primary_key=True)
    PBID = Column(Integer, nullable=False)
    CAC = Column(NVARCHAR(100), nullable=False)
    CAD = Column(NVARCHAR(100))
    CAE = Column(NVARCHAR(100))
    MARK = Column(TEXT)
    ND_TRAN = Column(NCHAR(1))
    PBZST_ID = Column(Integer)
    PBZST_P = Column(Numeric(5,1))
    PBZST_B = Column(TEXT)
    BEKANT_D = Column(DateTime, default=datetime.datetime.now)
    INS_D = Column(DateTime, default=datetime.datetime.now)
    UPD_D = Column(DateTime)

    def __repr__(self):
        return '<CA:%s>' % self.CAC

    def __str__(self):
        return self.CAC


class MA(Base):

    __tablename__ = 'MA'

    id = Column(Integer, primary_key=True)
    CAID = Column(Integer, nullable=False)
    MAC = Column(NVARCHAR(100), nullable=False)
    MAD = Column(NVARCHAR(100))
    MAE = Column(NVARCHAR(100))
    MARK = Column(TEXT)
    FAP_KZ = Column(NCHAR(1))
    ND_TRAN = Column(NCHAR(1))
    MA_STT = Column(Integer)
    MATP_ID = Column(Integer)
    MAPRIO = Column(Integer)
    TEMP_KZ = Column(NCHAR(1))
    PLV_ID = Column(Integer)
    TERMIN = Column(DateTime)
    BW_TXT = Column(TEXT)
    BW_D = Column(DateTime)
    BW_UPD_D = Column(DateTime)
    INS_D = Column(DateTime)
    UPD_D = Column(DateTime)
    BEKANT_D = Column(DateTime)


class MAIMP(Base):

    __tablename__ = 'MAIMP'

    id = Column(Integer, primary_key=True)
    MAID = Column(Integer, nullable=False)
    MARK = Column(Integer, nullable=False)
    BEGIN_D = Column(DateTime)
    VIN = Column(NCHAR(17))
    AEKO = Column(NVARCHAR(50))
    PLANT = Column(NVARCHAR(5))
    PLV_TXT = Column(NVARCHAR(100))
    INS_D = Column(DateTime)
    UPD_D = Column(DateTime)
    # PB_STT



