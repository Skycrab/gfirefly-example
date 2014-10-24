#coding:utf8

if __name__=="__main__":
    from gfirefly.master.master import Master
    master = Master()
    master.config('config.json','appmain.py')
    master.start()
    
    