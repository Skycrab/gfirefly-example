#coding:utf8
'''
Created on 2014-8-11

@author: skycrab68@163.com
'''

from gfirefly.server.globalobject import GlobalObject, netserviceHandle


"""
net默认service是CommandService(文件server/server.py)
	netservice = services.CommandService("netservice")
所以通过'_'分隔命令号

参数选项是通过函数doDataReceived传过来的(文件netconnect/protoc.py)
	def doDataReceived(self,conn,commandID,data):
        '''数据到达时的处理'''
        response = self.service.callTarget(commandID,conn,data)
        return response
"""

@netserviceHandle
def nethandle_100(_conn, data):
    """
    conn是LiberateProtocol的实例(netconnect/protoc.py)
    """
    print "handle_100:",data
    return "nethandle_100 ok"

@netserviceHandle
def nethandle_200(_conn, data):
    """200消息请求转发给gateserver处理
    remote['gate']是RemoteObject的实例(distributed/node.py)
    """
    return GlobalObject().remote['gate'].callRemote("gatehandle",data)

@netserviceHandle
def nethandle_300(_conn, data):
    """300消息请求转发给gateserver处理,gate再调用game1
    remote['gate']是RemoteObject的实例(distributed/node.py)
    """
    return GlobalObject().remote['gate'].callRemote("game1handle",data)


