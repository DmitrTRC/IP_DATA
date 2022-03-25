import ipaddress
import folium
import os
import socket
import requests
import webbrowser

from pyfiglet import Figlet
from termcolor import colored


# FIXME: Exception handling for invalid IP / URL
# TODO: Add question to save map to file
def validate_ip_address(address) -> bool:
    status = False  # False = invalid, True = valid
    try:
        ip = ipaddress.ip_address(address)
        status = True
    except ValueError:
        print(colored(f'Trying to validate {address}', 'yellow'))
        status = False
    finally:
        return status


def get_ip_from_url(url):
    ip = socket.gethostbyname(url)
    return ip


def get_local_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip


def get_global_ip():
    url = 'https://api.ipify.org?format=json'
    response = requests.get(url).json()
    return response.get('ip')


def get_ip_data(ip):
    url = f'http://ip-api.com/json/{ip}'
    response = requests.get(url).json()
    data = {
        'IP': response.get('query'),
        'City': response.get('city'),
        'Region': response.get('regionName'),
        'Country': response.get('country'),
        'Latitude': response.get('lat'),
        'Longitude': response.get('lon'),
        'Timezone': response.get('timezone'),
        'Internet Service Provider': response.get('isp'),
        'Organization': response.get('org'),
        'ZIP Code': response.get('zip'),
        }
    return data


def print_ip_info(data):
    for key, value in data.items():
        print(f'{key} : {value}')


def save_ip_map(data):
    area = folium.Map(location=[data['Latitude'], data['Longitude']], zoom_start=10)
    folium.Marker([data['Latitude'], data['Longitude']], popup=data['IP']).add_to(area)
    file_name = f'{data["City"]}_{data["IP"]}.html'
    area.save(file_name)
    print(colored(f'Map saved to {file_name}', 'green'))
    answer = input('Do you want to open the map? (y/n) ')
    if answer.lower() == 'y':
        webbrowser.open('file://' + os.path.realpath(file_name), new=2)


def show_own_ip_info():
    print('My LOCAL IP address:')
    print(get_local_ip())
    print('My GLOBAL IP address:')
    print(get_global_ip())


def greeting():
    welcome_message = Figlet(font='slant').renderText('IP - INFO', )
    print(colored(welcome_message, 'cyan'))


def main():
    greeting()
    show_own_ip_info()

    url = input("Enter URL / IP : ")
    ip = ''
    if not validate_ip_address(url):
        ip = get_ip_from_url(url)
    info = get_ip_data(ip)
    if info:
        print_ip_info(info)
        save_ip_map(info)
    else:
        print("No data found")


if __name__ == '__main__':
    main()
