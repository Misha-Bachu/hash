import hashlib
import pandas as pd
import time

def first_meth():
	data = pd.read_csv('10000001.txt',header = None,names=['password'])
	for i in data['password']:
		print(i)

def second_meth():
	with open('10000001.txt','r') as file:
		test = file.read()
	test = test.split('\n')
	for i in test:
		print(i)

time_first_fun = time.time()
first_meth()
time_first_fun = time.time() - time_first_fun

time_second_fun = time.time()
second_meth()
time_second_fun = time.time() - time_second_fun

print(f'first time = {time_first_fun}\nsecond time = {time_second_fun}')

# h = 'EA580646D2BF8AF82895D22BF3C8F1B4'
# print(h.lower() == hashlib.md5('Z6NGH58o'.encode('utf-8')).hexdigest())
