class Config:
    version = 0.1
    logo: str = """
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
    description = """
    If you have a folder with media files, but you don't want to extract from
    there manually, this script will help you extract all media data
    automatically. It searches for all the formats you need recursively,
    creates a folder for each format separately, and copies them there\n""".upper()

    @staticmethod
    def get_logo() -> None:
        print(Config.logo)

    @staticmethod
    def get_description() -> None:
        print(Config.description)

    @staticmethod
    def get_version():
        print('\t\t\t\t\t\t\t\t\t', Config.version)