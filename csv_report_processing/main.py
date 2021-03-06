from pyfiglet import figlet_format
from termcolor import colored
import os.path
import string
import random

from modules.process_file import process_file

header = colored(figlet_format('CSV REPORT PROCESSING'), color='cyan')
print(header)
print('\n=================================================================\n')


def init():
    """This function will initialise program"""

    file = input('Enter path to .csv file you wanna reorganize:\n')
    new_file_name = input('Enter name of new .csv file:\n')

    if os.path.isfile(f'./processed_files/{new_file_name}.csv'):     # Change name of file to prevent overwriting

        new_file_name = 'random_' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7)) # generate random string
        print(colored(f'File with such name exist! Name of your file is changed to: {new_file_name}', color='yellow'))

    elif not new_file_name:                                         # Set default name if nothing passed
        new_file_name += 'new_file'

    process_file(file, new_file_name)


init()
