from base import Base


def main():
    Base.get_logo()
    Base.get_description()

    """ Get path from user """
    path_to = Base.get_path()

    """ Creating Base instances """
    audio_instance = Base('Audios', 'audio_folder')
    video_instance = Base('Videos', 'video_folder')
    pictures_instance = Base('Pictures', 'images_folder')

    """ Adding media files if founding """
    audio_instance.add_storage(path_to, Base.audio_format)
    video_instance.add_storage(path_to, Base.video_format)
    pictures_instance.add_storage(path_to, Base.pictures_format)

    """ Extracting media files, each instance is responsible for its own format """
    audio_instance.extract_files()
    video_instance.extract_files()
    pictures_instance.extract_files()


if __name__ == '__main__':
    main()
