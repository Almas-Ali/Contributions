'''
Github Contribution Stealer script. With this you can make much contribution in no time.
Use it and enjoy.
'''

import os
from datetime import datetime as dt
import random
import string

# strftime('%a %b %e %H:%M:%S %Y %z')


def worker(filename: str, filecontent: str, adderstring: str, removerstring: str, dates: dict):
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
    os.system(f"git commit --amend --no-edit --date '{dates.get('dateName')} {dates.get('month')} {dates.get('date')} {time} {dates.get('year')} +0600' ")
    print(f"{dates.get('dateName')} {dates.get('month')} {dates.get('date')} {time} {dates.get('year')} +0600")


def NameMaker():
    alpha = string.ascii_letters + string.ascii_letters + string.ascii_letters
    name = ''.join(random.sample(alpha, 20))
    description = ''.join(random.sample(alpha, 50))

    return {
        'name': name,
        'description': description
    }


if __name__ == '__main__':
    commits = int(input('How many commits you need (1-99999): '))
    date = int(input('In which date you need (1-31): '))
    dateName = input('In which date you need (Sat-Fri): ')
    month = input('In which month you need (Jan-Dec): ')
    year = int(input('In which year you need (2022): '))

    # commits  = int(input('How many commits you need per day (1-99999): '))
    # year 	 = int(input('In which year you need (2022): '))

    dates = {
        'date': date,
        'dateName': dateName,
        'month': month,
        'year': year
    }

    try:
        for i in range(commits):
            # define jobs here...
            # worker(
            # 	filename='README.md',
            # 	filecontent='# This is the documentation of this project.',
            # 	adderstring='Added Docs',
            # 	removerstring='Removed Docs',
            # 	dates=dates
            # 	)
            # worker(
            # 	filename='contribution.md',
            # 	filecontent='# This is the contribution file of this project.',
            # 	adderstring='Added Contribution file.',
            # 	removerstring='Removed Contribution file.',
            # 	dates=dates
            # 	)
            names = NameMaker()
            worker(
                filename=names.get('name'),
                filecontent=f'# {names.get("description")}',
                adderstring=f'Added {names.get("name")} file.',
                removerstring=f'Removed {names.get("name")} file.',
                dates=dates
            )
            print(f'Done {i}')

    except KeyboardInterrupt as e:
        # Pushing it to github.
        print('[!] Stopting running process...')
    os.system('git push -u origin master')
