import os

from .discover import discover
from .crawl import crawl


def add_dictionary():
    """This function will handle adding new dictionary with subdomain names"""
    name = input('Enter name of new dict:\n')
    path = input('Enter path to the dict you wanna upload:\n')

    if os.path.exists(path):            # Check if the file exists
        try:
            with open(f'./dict/{name}.log', 'w+') as new_file, open(path) as old_file:
                r = old_file.read()
                new_file.write(r)
        except:
            print('Cannot resolve')
    else:
        print('\nCannot find that file')


def search():
    """This function will init proper searching-mode (which the user chose)"""
    print('Which searching mode you wanna use?\n')
    print('1 - Crawl\n')
    searching_mode = input('2 - Discover hidden sub-domains\n')

    if searching_mode == '1':
        crawl()
    elif searching_mode == '2':
        discover()
    else:
        print('Invalid data')
