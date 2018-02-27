import json
import sys
import re
from math import sqrt


def load_data_bars(file_path):
    with open(file_path, encoding='utf8') as file_data:
        return json.loads(file_data.read())


def get_biggest_bar(bars_list):
    return min(
        bars_list,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )


def get_smallest_bar(bars_list):
    return max(
        bars_list,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )


def get_closest_bar(bars_list, user_latitude, user_longitude):
    return min(
        bars_list,
        key=lambda x: sqrt(
            (x['geometry']['coordinates'][1] - user_latitude) ** 2 +
            (x['geometry']['coordinates'][0] - user_longitude) ** 2
        )
    )


def get_input_coordinates(*arg):
    coordinate_list = list()
    for name_coordinate in arg:
        coordinate = input('Enter {0}: '.format(name_coordinate))
        if re.match('^\d+?\.\d+?$', coordinate) is not None:
            coordinate_list.append(float(coordinate))
        else:
            raise TypeError
    return tuple(coordinate_list)


def print_answer(bar, description):
    contacts = bar['properties']['Attributes']
    delimiter = '-' * 50
    print(delimiter)
    print('Most {2} bar\nName: {0}\nAddress: {1}'.format(
        contacts['Name'],
        contacts['Address'],
        description
    ))
    print(delimiter)


if __name__ == '__main__':
    try:
        bars_list = load_data_bars(sys.argv[1])['features']
        biggest_bar = get_biggest_bar(bars_list)
        smallest_bar = get_smallest_bar(bars_list)
        longitude, latitude = get_input_coordinates('latitude', 'longitude')
        closest_bar = get_closest_bar(bars_list, longitude, latitude)
        print_answer(closest_bar, 'closest')
        print_answer(biggest_bar, 'biggest')
        print_answer(smallest_bar, 'smallest')
    except (FileNotFoundError, IndexError):
        sys.exit('File on the entered path was not found')
    except json.decoder.JSONDecodeError:
        sys.exit('File on the entered path not valid JSON format')
    except TypeError:
        sys.exit('Waiting float number')
