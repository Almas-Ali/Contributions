import os
import glob


def main():
	file = 'README.md'
	with open(file, 'a') as docs:
		docs.write('# This is the documentation of this project.')

	os.system('git add .')
	os.system('git commit -m "Added Docs." ')

	os.remove(file)

	os.system('git add .')
	os.system('git commit -m "Removed Docs." ')



if __name__ == '__main__':
	for i in range(1000):
		main()
		print(f'Done {i}')

	os.system('git push -u origin master')

