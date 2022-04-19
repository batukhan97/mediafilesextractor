from src.base import Base
from src.formats import Format
from src.settings import Config


def main():
    Config.get_logo()
    Config.get_description()

    """ Get path from user """
    path_to = Base.get_path()

    """ Creating format instance"""
    format = Format()

    """ Creating Base instances """
    audio_instance = Base('Audios', 'audio_folder')
    video_instance = Base('Videos', 'video_folder')
    pictures_instance = Base('Pictures', 'images_folder')

    """ Adding media files if founding """
    audio_instance.add_storage(path_to, format.audio_format)
    video_instance.add_storage(path_to, format.video_format)
    pictures_instance.add_storage(path_to, format.pictures_format)

    """ Extracting media files, each instance is responsible for its own format """
    audio_instance.extract_files()
    video_instance.extract_files()
    pictures_instance.extract_files()


if __name__ == '__main__':
    main()
