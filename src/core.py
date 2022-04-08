import os
import shutil
from colorama import Fore


class Base:
    def __init__(self, name, folder_name):
        self.name = name
        self.folder_name = folder_name
        self.path_storage = {}

    @staticmethod
    def get_path() -> str:
        while True:
            path = input(Fore.CYAN + '\tpath to folder: ')
            if os.path.exists(path):
                return path
            else:
                print(Fore.RED + f'\n\tinvalid path, try again'
                                 f'\n\texample -> /Users/zhandos256/Desktop/Takeout\n')

    def add_storage(self, path, format: tuple) -> None:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(format):
                    self.path_storage[file] = os.path.join(root, file)

    def check_storage(self) -> None:
        if len(self.path_storage) > 0:
            print(Fore.YELLOW + f'\tFounding {len(self.path_storage)} {self.name} files!')
        else:
            pass

    def extract_files(self) -> None:
        if len(self.path_storage) > 0:
            if not os.path.exists(self.folder_name):
                os.mkdir(self.folder_name)
                for file, path in self.path_storage.items():
                    target_path = os.path.join(os.getcwd(), self.folder_name, file)
                    shutil.copy2(path, target_path)
                print(Fore.GREEN + f'\t{self.name} copying success!')
        else:
            print(Fore.YELLOW + f'\t{self.name} files not found!')