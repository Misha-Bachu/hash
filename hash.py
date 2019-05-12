import time
import rarfile

upp = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
file_name_1 = './Variant01_1.rar'
file_name_2 = './Variant01_2.rar'
rarfile.UNRAR_TOOL='./unrar.exe'

def first_meth():
	time_first = time.time()
	file = rarfile.RarFile(file_name_1)
	for i0 in upp:
		for i1 in upp:
			for i2 in upp:
				for i3 in upp:
					word = i0+i1+i2+i3
					try:
						file.extractall(pwd=word, path='./Folder')
						file_save('firs_answer.txt',word,(time.time() - time_first))
						return
					except rarfile.RarCRCError:
						pass
					for i4 in upp:
						try:
							file.extractall(pwd=word+i4, path='./Folder')
							file_save('firs_answer.txt',word+i4,(time.time() - time_first))
							return
						except rarfile.RarCRCError:
							pass

def file_save(filename,pas,t):
	with open(filename, 'w+') as savefile:
		savefile.write(f'{pas} = {t}')
	print(f'{pas} = {t}')

first_meth()