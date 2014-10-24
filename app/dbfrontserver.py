#coding:utf8
'''
Created on 2014-8-11

@author: skycrab68@163.com
'''
from gfirefly.server.globalobject import GlobalObject

def doWhenStop():
    """服务器关闭前的处理
    """
    print '############'
    print 'server stop'

def init():
    GlobalObject().stophandler = doWhenStop