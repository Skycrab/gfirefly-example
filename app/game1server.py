#coding:utf8
'''
Created on 2014-8-11

@author: skycrab68@163.com
'''
from gfirefly.server.globalobject import GlobalObject, remoteserviceHandle

"""
"""
@remoteserviceHandle("gate")
def game1end(data):
	print "game1end handle",data
	return "game1end ok"