import os
import sys
import json
import math

class AutoAllocation:

	def __init__(self,latitude,longitude):
		self.latitude		= latitude
		self.longitude		= longitude
		self.R 				= 6373.0
		self.distance_data	= []

		self.distance_calculation()

	def distance_calculation(self):
		#read data from json
		loads 	= open("data.json")
		data 	= json.load(loads)

		#using Haversine formula for the distance calculation

		for item in data:
			temp = {}
			dlat = math.radians(self.latitude) - math.radians(item["latitude"])
			dlon = math.radians(self.longitude) - math.radians(item["longitude"])
			a = math.sin(dlat / 2)**2 + math.cos(math.radians(self.longitude)) * math.cos(math.radians(item["longitude"])) * math.sin(dlon / 2)**2
			c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

			distance = self.R * c

			temp["latitude"] 	= item["latitude"]
			temp["longitude"]	= item["longitude"]
			temp["distance"]	= distance

			self.distance_data.append(temp)
		print(sorted(self.distance_data, key=lambda key: key["distance"]))

	# def sort_the_array(self,reverse=False):
	# 	sort = self.distance_data.sort(key=lambda x: x.distance, reverse=True)
	# 	print(sort)





if __name__ == "__main__":
	allocation = AutoAllocation(12.9516,80.1462)