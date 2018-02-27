import json
import sys
import re
from math import sqrt

AVAILABLE_COMMANDS = ['1', '2', '3', 'q']


def load_data_bars(file_path):
    with open(file_path, encoding='utf8') as file_data:
        return json.loads(file_data.read())


def get_biggest_bar(bars_data):
    return min(
        bars_data['features'],
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )


def get_smallest_bar(bars_data):
    return max(
        bars_data['features'],
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )


def get_closest_bar(bars_data, user_latitude, user_longitude):
    return min(
        bars_data['features'],
        key=lambda x: sqrt(
            (x['geometry']['coordinates'][1] - user_latitude) ** 2 +
            (x['geometry']['coordinates'][0] - user_longitude) ** 2
        )
    )


def get_user_choose():
    print_for_user = (
        'Enter "1" - find the biggest bar in Moscow\n'
        'Enter "2" - find the smallest bar in Moscow\n'
        'Enter "3" - find the closest bar by gps coordinates\n'
        'Enter "q" - for log off the program\n'
        'Enter: '
    )
    while True:
        user_input = input(print_for_user)
        if user_input in AVAILABLE_COMMANDS:
            break
        print('\nNot available commands. Try again.\n')
    return user_input


def get_user_coordinates(*arg):
    coordinate_list = list()
    for name_coordinate in arg:
        while True:
            coordinate = input('Enter {0}: '.format(name_coordinate))
            if not re.match('^\d+?\.\d+?$', coordinate) is None:
                coordinate_list.append(float(coordinate))
                break
            print('\nCorrectly value format: **.*******\n')
    return tuple(coordinate_list)


def processing_choose(user_choose, bars_data):
    if user_choose == 'q':
        raise SystemExit
    elif user_choose == '1':
        return get_biggest_bar(bars_data)
    elif user_choose == '2':
        return get_smallest_bar(bars_data)
    elif user_choose == '3':
        longitude, latitude = get_user_coordinates('latitude', 'longitude')
        return get_closest_bar(bars_data, longitude, latitude)


def print_answer(bar):
    contacts = bar['properties']['Attributes']
    print('-' * 50)
    print('Name: {0}\nAddress: {1}'.format(
        contacts['Name'],
        contacts['Address']
    ))
    print('-' * 50)


if __name__ == '__main__':
    try:
        path_bar_data = input('Enter path to file: ')
        bars_data = load_data_bars(path_bar_data)
        necessary_bar = processing_choose(get_user_choose(), bars_data)
        print_answer(necessary_bar)
    except FileNotFoundError:
        sys.exit('File on the entered path was not found')
    except json.decoder.JSONDecodeError:
        sys.exit('File on the entered path not JSON format')
    except SystemExit:
        sys.exit('Good bay! See you soon!')
