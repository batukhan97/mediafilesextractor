import os
import shutil
import sys

from colorama import Fore
from src.settings import Config
from src.formats import Format

audio_storage = {}
video_storage = {}
pictures_storage = {}


def get_path() -> str:
    """ Having path in user and return it """
    while True:
        path_to = input(Fore.CYAN + '\tpath to folder: ')
        if os.path.exists(path_to):
            return path_to
        else:
            print(Fore.RED + '\n\tInvalid path, try again\n\texample -> /Users/User/Desktop/somefolder\n')


def broot_dirs(path: str) -> None:
    """ Broot dirs and if have files, adding to storages"""
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(Format.audio_format):
                audio_storage[file] = os.path.join(root, file)
            if file.endswith(Format.video_format):
                video_storage[file] = os.path.join(root, file)
            if file.endswith(Format.pictures_format):
                pictures_storage[file] = os.path.join(root, file)


def print_res() -> None:
    """ Print some results if found media files """
    print('')
    if len(audio_storage) > 0:
        print(Fore.YELLOW + f'\tFound {len(audio_storage)} audio files!')
    if len(video_storage) > 0:
        print(Fore.YELLOW + f'\tFound {len(video_storage)} video files!')
    if len(pictures_storage) > 0:
        print(Fore.YELLOW + f'\tFound {len(pictures_storage)} picture files!')
    print('')


def extract() -> None:
    """ If founding media files, creating folders and extract files to folder """
    confirm = input(Fore.YELLOW + '\tDo you wanna extract him? : Y/n : ')
    print('')
    if confirm not in ['yes', 'Yes', 'YES', 'y', 'Y']:
        print(Fore.GREEN + '\n\texit...\n')
        sys.exit()

    # this block work with audio storage
    if len(audio_storage) > 0:
        folder_name = 'audio_files'
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            for file, path in audio_storage.items():
                target_path = os.path.join(os.getcwd(), folder_name, file)
                shutil.copy2(path, target_path)
        print(Fore.GREEN + '\tAudio files extract success!')

    # this block work with video storage
    if len(video_storage) > 0:
        folder_name = 'video_files'
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            for file, path in video_storage.items():
                target_path = os.path.join(os.getcwd(), folder_name, file)
                shutil.copy2(path, target_path)
        print(Fore.GREEN + '\tVideo files extract success!')

    # this block work with picture storage
    if len(pictures_storage) > 0:
        folder_name = 'pictures_files'
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            for file, path in pictures_storage.items():
                target_path = os.path.join(os.getcwd(), folder_name, file)
                shutil.copy2(path, target_path)
        print(Fore.GREEN + f'\tPictures files extract success!')
    print('')


def main() -> None:
    Config.get_logo()
    path_from_user = get_path()
    broot_dirs(path_from_user)
    print_res()
    extract()


if __name__ == '__main__':
    main()
