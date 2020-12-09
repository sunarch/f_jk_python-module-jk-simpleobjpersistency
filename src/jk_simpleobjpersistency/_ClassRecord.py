

import os
import types





class _ClassRecord(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self, clazz:type, dirPath:str, defaults:dict):
		self.clazz = clazz
		self.dirPath = dirPath
		self.defaults = defaults
		self.__nNextIdentifier = None
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def findFreeIdentifier(self):
		if self.__nNextIdentifier is None:
			self.__nNextIdentifier = 1
		while True:
			filePath = os.path.join(self.dirPath, "id" + str(self.__nNextIdentifier) + ".json")
			if not os.path.exists(filePath):
				ret = "id" + str(self.__nNextIdentifier)
				self.__nNextIdentifier += 1
				return ret
	#

#








