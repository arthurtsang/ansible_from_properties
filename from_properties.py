#!/usr/bin/python
import pyjq

def from_properties(properties):
	json = {}
	propertyLines = properties.split('\n')
	for propertyLine in propertyLines:
		keyValue = propertyLine.split('=')
		json = pyjq.all("."+keyValue[0]+'="'+keyValue[1]+'"',json)[0]
	return json

class FilterModule(object):
	def filters(self):
		return {
			'from_properties': from_properties,
		}
