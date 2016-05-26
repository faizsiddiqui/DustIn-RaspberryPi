'''
@task	: 	REST client to send and recieve data from the server
'''

import json
import requests

class REST:

	def __init__(self, baseURL, timeout):
		self.baseURL = baseURL
		self.headers = {'user-agent': 'DUSTIN/0.0.1'}
		self.timeout = timeout

	def get(self, resource):
		response = requests.get(self.baseURL + resource, headers=self.headers, timeout=self.timeout)
		if response.status_code != 200:
			raise ApiError('GET {} {}'.format(resource, response.status_code))
		return response.json()
		'''try:
		    response = requests.get(self.baseURL + resource, headers=self.headers, timeout=self.timeout)
			if response.status_code != 200:
				raise ApiError('GET {} {}'.format(resource, response.status_code))
			return response.json()
		except requests.exceptions.Timeout:
			print "Connection timeout!"
		except requests.exceptions.TooManyRedirects:
			print "Too Many Redirects!"
		except requests.exceptions.RequestException as e:
		    print e
		finally:
			print "Exiting!"'''

	def post(self, resource, data):
		response = requests.post(self.baseURL + resource, data=data, headers=self.headers, timeout=self.timeout)
		if response.status_code != 200:
			raise ApiError('POST {} {}'.format(resource, response.status_code))
		return response.json()
		'''try:
		    response = requests.post(self.baseURL + resource, data=data, headers=self.headers, timeout=self.timeout)
			if response.status_code != 200:
				raise ApiError('POST {} {}'.format(resource, response.status_code))
			return response.json()
		except requests.exceptions.Timeout:
			print "Connection timeout!"
		except requests.exceptions.TooManyRedirects:
			print "Too Many Redirects!"
		except requests.exceptions.RequestException as e:
		    print e
		finally:
			print "Exiting!"'''
