import configparser

config = configparser.RawConfigParser()

config.read("C:\\Users\\Suyash\\Desktop\\CREDENCE CLASS\\Pycharm Program\\OrangeHRM by Me\\Configuration\\Config.ini")


class ReadValue():

    @staticmethod
    def getUsername():
        username = config.get("login info", 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('login info', 'password')
        return password

    @staticmethod
    def getUrl():
        url = config.get('login info', 'Url')
        return url

