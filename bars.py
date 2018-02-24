import json
import sys
import re

PATH_TO_FILE = 'bar_moscow_json'
# PATH_TO_SEATS_COUNT = ['features']['properties']['Attributes']['SeatsCount']
AVAILABLE_COMMANDS = ['1', '2', '3', 'exit']


def load_data(filepath):
    with open(filepath) as file_data:
        return json.loads(file_data.read())


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


def get_user_input():
    print_for_user = (
        'Enter "1" - find the biggest bar in Moscow\n'
        'Enter "2" - find the smallest bar in Moscow\n'
        'Enter "3" - find the closest bar by gps coordinates\n'
        'Enter "exit" - for log off the program\n'
        'Enter: '
    )
    while True:
        user_input = input(print_for_user)
        if user_input in AVAILABLE_COMMANDS:
            break
    return user_input


def get_user_coordinates(*arg):
    coordinate_list = list()
    for name_coordinate in arg:
        while True:
            coordinate = input('Enter {0}: '.format(name_coordinate))
            if not re.match('^\d+?\.\d+?$', coordinate) is None:
                coordinate_list.append(float(coordinate))
                break
    return tuple(coordinate_list)


if __name__ == '__main__':
    bar_data = load_data(PATH_TO_FILE)
    user_choose = get_user_input()
    if user_choose == 'exit':
        sys.exit('Good bay! See you later!')
    elif user_choose == '1':
        print(get_biggest_bar(bar_data))
    elif user_choose == '2':
        print(get_smallest_bar(bar_data))
    elif user_choose == '3':
        longitude, latitude = get_user_coordinates('longitude', 'latitude')
        print(get_closest_bar(bar_data, longitude, latitude))
