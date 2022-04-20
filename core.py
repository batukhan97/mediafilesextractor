import os
from sys import exit
from shutil import copy2


class Base:
    """ Script help you automatically extract your media files from folders """

    __logo: str = """
        ███╗░░░███╗███████╗██████╗░██╗░█████╗░  ███████╗██╗██╗░░░░░███████╗░██████╗
        ████╗░████║██╔════╝██╔══██╗██║██╔══██╗  ██╔════╝██║██║░░░░░██╔════╝██╔════╝
        ██╔████╔██║█████╗░░██║░░██║██║███████║  █████╗░░██║██║░░░░░█████╗░░╚█████╗░
        ██║╚██╔╝██║██╔══╝░░██║░░██║██║██╔══██║  ██╔══╝░░██║██║░░░░░██╔══╝░░░╚═══██╗
        ██║░╚═╝░██║███████╗██████╔╝██║██║░░██║  ██║░░░░░██║███████╗███████╗██████╔╝
        ╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═════╝░

        ███████╗██╗░░██╗████████╗██████╗░░█████╗░░█████╗░████████╗░█████╗░██████╗░
        ██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
        █████╗░░░╚███╔╝░░░░██║░░░██████╔╝███████║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝
        ██╔══╝░░░██╔██╗░░░░██║░░░██╔══██╗██╔══██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗
        ███████╗██╔╝╚██╗░░░██║░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║
        ╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
        """

    __description = """
        If you have a folder with media files, but you don't want to extract from
        there manually, this script will help you extract all media data
        automatically. It searches for all the formats you need recursively,
        creates a folder for each format separately, and copies them there\n"""

    audio_format = (
    '.wav', '.flac', '.mp3', '.ogg', '.m3u', '.acc', '.wma', '.midi', '.aif', '.m4a', '.m4a', '.mpa',
    '.pls', '.shn', '.ape', '.wv', '.tta', '.spx')

    video_format = (
    '.mov', '.swf', '.mp4', '.mkv', '.flv', '.wmv', '.avi', '.3gp', '.vob', '.aaf', '.mod', '.mpeg',
    '.webm', '.f4v', '.swf')

    pictures_format = (
    '.mbp', '.jpg', '.png', '.raw', '.psd', '.eps', '.gif', '.ico', '.ai', '.svg', '.tif', '.cdr')

    def __init__(self, name, folder_name):
        self.name = name
        self.folder_name = folder_name
        self.path_storage = {}

    @staticmethod
    # get path from user and return it to next func
    def get_path() -> str:
        try:
            while True:
                path = input('\tPATH TO FOLDER: ')
                if os.path.exists(path):
                    return path
                else:
                    print(f'\n\tpath does not exists, try again'
                          f'\n\texample -> /Users/User/Desktop/Somefolder\n')
        except KeyboardInterrupt:
            exit()

    @staticmethod
    def get_logo():
        print(Base.__logo)

    @staticmethod
    def get_description():
        print(Base.__description)

    # get path from previous func and format in user, broot dirs and append it if found
    def add_storage(self, path, format: tuple) -> None:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(format):
                    self.path_storage[file] = os.path.join(root, file)

    # if files found, starting extract from self.path_storage
    def extract_files(self) -> None:
        if len(self.path_storage) > 0:
            if not os.path.exists(self.folder_name):
                print(f'\tFounding {len(self.path_storage)} {self.name} files!')
                os.mkdir(self.folder_name)
                for file, path in self.path_storage.items():
                    target_path = os.path.join(os.getcwd(), self.folder_name, file)
                    try:
                        copy2(path, target_path)
                    except FileNotFoundError:
                        continue
                    except PermissionError:
                        continue
                    except OSError:
                        continue
                print(f'\t{self.name} files copying success -> '
                      f'{os.path.join(os.getcwd(), self.folder_name)}')
            else:
                print(f'\t{self.folder_name} already exists!!!')
        else:
            print(f'\t{self.name} files not found!')
