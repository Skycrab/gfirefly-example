#coding:utf8
'''
Created on 2014-8-11

@author: skycrab68@163.com
'''
from gfirefly.server.globalobject import GlobalObject, rootserviceHandle

@rootserviceHandle
def gatehandle(data):
	print "gatehandle:",data
	return "gate ok"

@rootserviceHandle
def game1handle(data):
	print "gate forward to game1"
	return GlobalObject().root.callChild("game1","game1end",data)