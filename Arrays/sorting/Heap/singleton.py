class singleton_decorator(object):
    def __init__(self,instance_cls):
    	self.instance_cls=instance_cls
    	self.instance=None

    def __call__(self,*args,**kwargs):
    	if self.instance == None:
    		self.instance=self.instance_cls(*args,**kwargs)
    	return self.instance