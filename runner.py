#-*- coding: UTF-8 -*-
import os
import time
import datetime
from missing_check import jj_daily_check
from missing_check_stock import stockjj_daily_check
import cx_Oracle,sqlalchemy
import pandas as pd
import csv
from to__sql import ImportCSV

class CMD_jj():
    #------------------------------------------------------------------------------------添加每日基金净值到csv文件
    def add_jj_daily(self):
        os.system('cd C:\\Users\\Administrator\\PycharmProjects\\untitle4\\jijing')
        os.system('scrapy crawl jj_daily')
    #------------------------------------------------------------------------------------添加每日场内基金净值到csv文件
    def add_stockjj_daily(self):
        os.system('cd C:\\Users\\Administrator\\PycharmProjects\\untitle4\\jijing')
        os.system('scrapy crawl stockjj_daily')

    def add_equity_jj(self):
        os.system('cd C:\\Users\\Administrator\\PycharmProjects\\untitle5\\jijing')
        os.system('scrapy crawl jj_equity_')

    def add_equity_stockjj(self):#TODO
        os.system('cd C:\\Users\\Administrator\\PycharmProjects\\untitle5\\jijing')
        os.system('scrapy crawl jj_equity_')

def date_find():
    #-----------------------------------------------------------------------------------Finding date
    weekday = datetime.date.today().isoweekday()
    if weekday == 1:
        return str(datetime.date.today() - datetime.timedelta(days=3))
    else:
        return str(datetime.date.today() - datetime.timedelta(days=1))

class JJ_update():
    def update_jj_daily(self):
        #----------------------------------------------------------------------------------开放每日基金查漏
        totalcodes,missing,updated = jj_daily_check(date_find())
        while totalcodes < 2800:
            CMD_jj.add_jj_daily()
        #-----------------------------------------------------------------------------------如果有新基金了，找历史记录
        while missing != 0:
            CMD_jj.add_equity_jj()
        #--------------------------------------------------------------------------------------开放基金导入数据库
        to_sql = ImportCSV()
        to_sql.insert('C:\\Users\\Administrator\\PycharmProjects\\untitled4\\jijing\\过往基金净值extra.csv','jj_equity_data')
        to_sql.insert('C:\\Users\\Administrator\\PycharmProjects\\untitled4\\jijing\\开放基金每日净值.csv','jj_equity_data')

    def update_stockjj_daily(self):
        # ----------------------------------------------------------------------------------开放每日基金查漏
        totalcodes, missing, updated = stockjj_daily_check(date_find())
        while totalcodes < 2800:
            CMD_jj.add_jj_daily()
        # -----------------------------------------------------------------------------------如果有新基金了，找历史记录
        while missing != 0:
            add_equity_jj()
        # --------------------------------------------------------------------------------------开放基金导入数据库
        to_sql = ImportCSV()
        to_sql.insert('C:\\Users\\Administrator\\PycharmProjects\\untitled4\\jijing\\过往基金净值extra.csv', 'jj_equity_data')
        to_sql.insert('C:\\Users\\Administrator\\PycharmProjects\\untitled4\\jijing\\开放基金每日净值.csv', 'jj_equity_data')


class stock_update():
    pass