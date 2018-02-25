import json
import sys
import re
from functools import reduce


AVAILABLE_COMMANDS = ['1', '2', '3', 'exit']


def load_data(file_path):
    with open(file_path, encoding='utf8') as file_data:
        return json.loads(file_data.read())


def get_biggest_bar(data):
    return min(
        data['features'],
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )


def get_smallest_bar(data):
    return max(
        data['features'],
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )


def get_closest_bar(data, longitude, latitude):
    pass


def get_user_choose():
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


def processing_choose(user_choose, bars_data):
    if user_choose == 'exit':
        return None
    elif user_choose == '1':
        return get_biggest_bar(bars_data)
    elif user_choose == '2':
        return get_smallest_bar(bars_data)
    elif user_choose == '3':
        longitude, latitude = get_user_coordinates('longitude', 'latitude')
        return get_closest_bar(bars_data, longitude, latitude)


if __name__ == '__main__':
    try:
        path_bar_data = input('Enter path to file: ')
        bars_data = load_data(path_bar_data)
        necessary_bar = processing_choose(get_user_choose(), bars_data)
        if necessary_bar is None:
            sys.exit('Good bay! See you soon!')
        else:
            print(necessary_bar)
    except FileNotFoundError:
        sys.exit('File on the entered path was not found. '
                 'Check path to file.')
    except json.decoder.JSONDecodeError:
        sys.exit('File on the entered path not JSON format')
