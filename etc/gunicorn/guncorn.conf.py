# -*- coding: utf-8 -*-
# gunicorn.py
import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os
import multiprocessing

bind = "0.0.0.0:8000"	#绑定ip和端口号

backlog = 1024 #监听队列

workers = multiprocessing.cpu_count() * 2 + 1    #进程数
threads = 2 #指定每个进程开启的线程数

loglevel = 'info'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'    #设置gunicorn访问日志格式，错误日志无法设置

accesslog = "/var/log/gunicorn/access.log"      #访问日志文件
errorlog = "/var/log/gunicorn/error.log"        #错误日志文件

chdir = '/root/workspace/lete'
timeout = 30
worker_class = 'gevent'

proc_name = 'fof_api'   #进程名