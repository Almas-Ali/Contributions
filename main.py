'''
Github Contribution Stealer script. With this you can make much contribution in no time.
Use it and enjoy.
'''

import os
from datetime import datetime as dt

# strftime('%a %b %e %H:%M:%S %Y %z')

def worker(filename:str, filecontent:str, adderstring:str, removerstring:str):
	# Opening files, writting contents and save it.
	with open(filename, 'a') as docs:
		docs.write(filecontent)

	# Adding it in git and commiting it.
	os.system('git add .')
	os.system(f'git commit -m "{adderstring}" ')

	# Removing it from system.
	os.remove(filename)

	time = dt.now().strftime('%H:%M:%S')

	# Adding remove descriptions and commiting it.
	os.system('git add .')
	os.system(f'git commit -m "{removerstring}" ')
	os.system(f'git commit -amend --date="Tue Aug 7 {time} 2022 +0600" ')


if __name__ == '__main__':
	try:
		for i in range(1000):
			#define jobs here...
			worker(
				filename='README.md',
				filecontent='# This is the documentation of this project.',
				adderstring='Added Docs',
				removerstring='Removed Docs'
				)
			worker(
				filename='contribution.md',
				filecontent='# This is the contribution file of this project.',
				adderstring='Added Contribution file.',
				removerstring='Removed Contribution file.'
				)
			print(f'Done {i}')

	except KeyboardInterrupt as e:
		# Pushing it to github.
		print('[!] Stopting running process...')
	os.system('git push -u origin master')

