#-*- coding: UTF-8 -*-
import os
import time
import datetime
from missing_check import jj_daily_check
from missing_check_stock import stockjj_daily_check
import cx_Oracle,sqlalchemy
import pandas as pd
import csv


class ImportOracle():
    def __init__(self):
        self.engine = sqlalchemy.create_engine('oracle://shuzeng:Shuzeng123@localhost:1521/orcl?charset=utf8')
    def insert(self,add,tablename = 'jj_equity_data'):
        pass

class ImportCSV(ImportOracle):
    def insert(self,add,tablename = 'jj_equity_data'):
        df = pd.read_csv(add,'rb')
        length = df.shape[0]
        for i in length:
            try:
                df[i:i+1].to_sql(tablename,self.engine,if_exists='append',index = False)
            except Exception:
                continue