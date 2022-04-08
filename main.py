from src.core import Base
from src.formats import Format
from src.settings import Config


def main():
    Config.get_logo()

    """ Get path from user """
    path_to = Base.get_path()

    """ Creating Base instances """
    audio_instance = Base('Audio', 'audio_folder')
    video_instance = Base('Video', 'video_folder')
    pictures_instance = Base('Image', 'images_folder')

    """ Adding media files if founding """
    audio_instance.add_storage(path_to, Format.audio_format)
    video_instance.add_storage(path_to, Format.video_format)
    pictures_instance.add_storage(path_to, Format.pictures_format)

    """ Check media files if found printing him """
    audio_instance.check_storage()
    video_instance.check_storage()
    pictures_instance.check_storage()

    """ Extracting media files, each instance is responsible for its own format """
    audio_instance.extract_files()
    video_instance.extract_files()
    pictures_instance.extract_files()


if __name__ == '__main__':
    main()
