from colorama import Fore


class Config:
    verison: float = 0.1
    description: str = ''''''
    logo: str = Fore.BLUE + """
    █▀▄▀█ █▀▀ █▀▀▄ ░▀░ █▀▀█ 　 █▀▀▄ █▀▀█ ▀▀█▀▀ █▀▀█ 
    █░▀░█ █▀▀ █░░█ ▀█▀ █▄▄█ 　 █░░█ █▄▄█ ░░█░░ █▄▄█ 
    ▀░░░▀ ▀▀▀ ▀▀▀░ ▀▀▀ ▀░░▀ 　 ▀▀▀░ ▀░░▀ ░░▀░░ ▀░░▀ 

    █▀▀ █░█ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ 
    █▀▀ ▄▀▄ ░░█░░ █▄▄▀ █▄▄█ █░░ ░░█░░ █░░█ █▄▄▀ 
    ▀▀▀ ▀░▀ ░░▀░░ ▀░▀▀ ▀░░▀ ▀▀▀ ░░▀░░ ▀▀▀▀ ▀░▀▀
    """

    @staticmethod
    def get_logo() -> None:
        print(Config.logo)