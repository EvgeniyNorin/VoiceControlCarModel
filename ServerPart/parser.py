# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import requests
import re
import random


class SimpleXmlParser:
	dictionary_tuple = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f") 

	def __key_generate(self):
		key_string = ""
		for i in range(0, 32):
			key_string += self.dictionary_tuple[random.randint(0, 15)]
		return key_string


	def parse(self, text):
		root = ET.fromstring(text.encode('utf-8	'))
		if root.attrib["success"] == "0":
			return ""
		else:
			return	root[0].text


			

	def request(self):
		url_string = "https://asr.yandex.net/asr_xml?uuid=" + self.__key_generate() + "&key=80242ad4-7ad2-4a56-bd7f-47bd861e1333&topic=queries"
		data = open('speech.wav').read()
		res = requests.post(url = url_string, data = data, headers = {'Content-Type': 'audio/x-wav'})
		return res.text

	def direction_parser(self, text):
			
		if text == "вперед".decode('utf-8'):
			return 8
		elif text == "назад".decode('utf-8'):
			return 2
		elif text == "влево".decode('utf-8'):
			return 4
		elif text == "вправо".decode('utf-8'):
			return 6

	def string_parser(self, text):
		list = re.split(' ', text)
		time_value = 0
		try:
			time_value = int(list[len(list)-1])
		except:
			return (0, time_value)
		if len(list) == 2:
			return (self.direction_parser(list[0]), time_value)
		if len(list) == 3:
			return (self.direction_parser(list[0]), self.direction_parser(list[1]), time_value)			


		