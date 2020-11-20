from collections import UserDict
class StrKeyDict(UserDict):
	def __missing__(self,key):
		if isinstance(key,str):
			raise KeyError(key)
		return self[str(key)]
	def __setitem__(self,key,item):
		self.data[str(key)]=item
	def __contains__(self,key):
		return str(key) in self.data
tst=StrKeyDict({1:1,'a':2})
print(tst.data,'a' in tst,1 in tst)

