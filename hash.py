import hashlib
import pandas as pd
import time

h = 'EA580646D2BF8AF82895D22BF3C8F1B4'.lower()

def first_meth():
	data = pd.read_csv('1000000.txt',header = None,names=['password'])
	for i in data['password']:
		res = hashlib.md5(str(i).encode('utf-8')).hexdigest()
		if h == res:
			print(f'{i} = {res}')
			break

time_first_fun = time.time()
first_meth()
time_first_fun = time.time() - time_first_fun

print(f'first time = {time_first_fun}')