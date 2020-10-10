import os
import sys
import json
import math

class AutoAllocation:

	def __init__(self,latitude,longitude,allocation_logic):
		self.latitude		= latitude
		self.longitude		= longitude
		self.R 				= 6373.0
		self.distance_data	= []
		self.sorted_array	= []
		self.output_data	= []
		self.allocation_logic = allocation_logic

		self.distance_calculation()

	def distance_calculation(self):
		#read data from json
		loads 	= open("data.json")
		data 	= json.load(loads)

		datas = list(filter(lambda x:x["id"]!=[1,2],data))
		print(datas)

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
		self.sort_the_array()
		#print(sorted(self.distance_data, key=lambda key: key["distance"]))

	def sort_the_array(self):
		self.sorted_array = sorted(self.distance_data, key=lambda key: key["distance"])
		self.data_collapse()

	def data_collapse(self):
		if(self.allocation_logic == 1):
			#send back to one data
			if len(self.sorted_array) > 0:
				self.output_data.append(self.sorted_array[0])
			else:
				self.output_data = []

		else:
			self.output_data = []






		