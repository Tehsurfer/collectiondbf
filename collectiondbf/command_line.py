import requests
from blackfynn import Blackfynn
from .config import API_TOKEN, API_SECRET
import os
import sys
import platform
import argparse
import json
import appdirs
from pathlib import Path
if platform != "darwin":
    from .ui import DetailsInput
import progressbar

def env_keys_valid():
    if API_TOKEN != 'local-api-key' and API_SECRET != 'local-secret-key':
        return True
    return False

def arg_valid():
    if len(sys.argv) == 1:
        return False
    if len(sys.argv[2].split('-')) == 5 and len(sys.argv[3].split('-')) == 5:
        return True
    return False

def run():

    args = argparse_setup()
    config = config_file()

    if len(sys.argv) == 1:
        if platform == "darwin":
            print('Sorry, tkinter in MacOS is not supported :(. Please use the CLI options')
            return
        ui = DetailsInput()
        api_token, api_secret, collection, args.recursive = ui.values()
        try:
            bf = Blackfynn(api_token=api_token, api_secret=api_secret)
            create_config_file(api_token, api_secret)
        except:
            if config:
                api_token = config['token']
                api_secret = config['secret']
    elif env_keys_valid():
        api_token = API_TOKEN
        api_secret = API_SECRET
        collection = args.id
    elif config:
        api_token = config['token']
        api_secret = config['secret']
        collection = args.id
    elif arg_valid():
        api_token = args.key
        api_secret = args.secret
        collection = args.id
        try:
            bf = Blackfynn(api_token=api_token, api_secret=api_secret)
            create_config_file(api_token, api_secret)
        except:
            pass
    print('Recursive downloads set to: ' + str(args.recursive))
    bf = Blackfynn(api_token=api_token,api_secret=api_secret)
    print('Connected to Blackfynn')

    print('Looking for Collection...')
    col = get_folder_items(bf, collection)
    print('Collection found. Staring file downloads...')
    get_files(col, recursive=args.recursive)


def get_file_type(s3_url):
    if (len(s3_url.split('.')) <= 2 and 'com' in s3_url) or len(s3_url.split('.')) == 1:
        return ''
    return s3_url.split('.')[-1]


def get_files(collection, recursive=False, file_path=''):
    Path(os.path.join(file_path, collection.name)).mkdir(parents=True, exist_ok=True)
    for item in progressbar.progressbar(collection.items):
        if recursive and not downloading_blackfynn_package(item, collection, file_path):
            get_files(item, recursive=True, file_path=os.path.join(file_path, collection.name))

def downloading_blackfynn_package(item, collection, file_path):
    if 'files' in dir(item):
        for file in item.files:
            file_type = get_file_type(file.s3_key)
            s3_url = file.url
            response = get_file_from_s3(s3_url, file.name)
            if response.status_code == 200:
                sys.stdout.write('\rDownloading file: %s' % file.name)
                f = open(os.path.join(file_path, collection.name, file.name + '.' + file_type), 'wb')
                f.write(response.content)
                sys.stdout.flush()
        return True
    return False

def get_file_from_s3(url, file_name=''):
    try:
        response = requests.get(url)
    except MemoryError:
        print(str(file_name) + ' was too big to fit into memory :( Skipping this file. ' +
                          'Feel free to download manually with this link: \n' + url)
    return response

def make_dir(dir_path):
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        pass


def get_folder_items(bf, name):
    if 'dataset' in name:
        return bf.get_dataset(name)
    return bf.get(name)


def argparse_setup():
    parser = argparse.ArgumentParser(description='Download datasets and folders from Blackfynn')
    parser.add_argument("id", nargs='?', type=str, help="This is the Package ID or Dataset ID associated with the"
                                                        "data you would like to download. Find it by checking the"
                                                        "URL of a dataset or folder you wish to download")
    parser.add_argument("key", nargs='?', type=str, help="This is the your Blackfynn 'API Token' key")
    parser.add_argument("secret", nargs='?', type=str, help="This is the your Blackfynn 'API Secret' key")

    parser.add_argument("--recursive", action="store_true", help="Set this value to true if you wish to download"
                                                                  "folders recursively")
    args = parser.parse_args()
    return args

def create_config_file(api_token, api_secret):
    CONFIG_DIR = Path(appdirs.user_config_dir(appname='collectiondbf'))  # magic
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    config = CONFIG_DIR / 'config.json'
    with config.open('w') as f:
            json.dump({'token':api_token,
                        'secret':api_secret}, f)

def config_file():
    CONFIG_DIR = Path(appdirs.user_config_dir(appname='collectiondbf'))  # magic
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    config = CONFIG_DIR / 'config.json'
    if config.exists():
        with config.open('r') as f:
            return json.load(f)
    else:
        return False