import os
import sys
import json
import math
from autoallocation import AutoAllocation

class allocation:
	def __init__(self,allocation_logic,latitude,longitude):
		self.allocation_logic 	= allocation_logic
		self.latitude 			= latitude
		self.longitude			= longitude

		self.autoallocation_execution()

	def autoallocation_execution(self):
		allocation = AutoAllocation(self.latitude,self.longitude,self.allocation_logic,[])
		print(allocation.output_data)



if __name__ == "__main__":
	allocation = allocation(1,12.9516,80.1462)

	