#!/usr/bin/python
import pyjq
import re

def from_properties(properties):
	json = {}
	propertyLines = properties.split('\n')
	for propertyLine in propertyLines:
		if propertyLine.startswith('#'):
			continue
		keyValue = propertyLine.split('=',1)
		json = pyjq.all("."+keyValue[0].strip()+'="'+re.escape(keyValue[1]).strip()+'"',json)[0]
	return json

class FilterModule(object):
	def filters(self):
		return {
			'from_properties': from_properties,
		}
