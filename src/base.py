import os
import sys
import shutil


class Base:
    def __init__(self, name, folder_name):
        self.name = name
        self.folder_name = folder_name
        self.path_storage = {}

    @staticmethod
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
            sys.exit()

    def add_storage(self, path, format: tuple) -> None:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(format):
                    self.path_storage[file] = os.path.join(root, file)

    def extract_files(self) -> None:
        if len(self.path_storage) > 0:
            if not os.path.exists(self.folder_name):
                print(f'\tFounding {len(self.path_storage)} {self.name} files!')
                os.mkdir(self.folder_name)
                for file, path in self.path_storage.items():
                    target_path = os.path.join(os.getcwd(), self.folder_name, file)
                    shutil.copy2(path, target_path)
                print(f'\t{self.name} files copying success -> '
                      f'{os.path.join(os.getcwd(), self.folder_name)}')
            else:
                print(f'\t{self.folder_name} already exists!!!')
        else:
            print(f'\t{self.name} files not found!')
