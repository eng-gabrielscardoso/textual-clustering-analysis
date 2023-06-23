import configparser
import os
import sys


class App:
    INI_FILE = "app.ini"

    def __load_ini_file(self, filename):
        full_path = os.path.abspath(os.path.join("./", filename))
        path_config_file = full_path if os.path.isfile(full_path) else \
            os.path.abspath(os.path.join(
                os.path.dirname(sys.executable), filename))
        self.config = configparser.ConfigParser()
        if self.config.read(path_config_file):
            return True
        else:
            print(f"Couldn't load file in {path_config_file}")
            return False

    def __load_file(self, filePaths):
        try:
            self.files = []
            for file in filePaths:
                full_path = os.path.abspath(
                    os.path.join("./src/assets/texts", file))
                path_words_file = full_path if os.path.isfile(full_path) else \
                    os.path.abspath(os.path.join(
                        os.path.dirname(sys.executable), file))
                with open(path_words_file, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.files.append(content)

            return True
        except Exception as e:
            print(f"Failed to open words file: {e}")
            return False

    def __init__(self) -> None:
        if self.__load_ini_file(self.INI_FILE):
            filePaths = self.config.get("assets", "files").split(",")
            if self.__load_file(filePaths):
                self.__run()

    def __run(self):
        try:
            print(
                f'{self.config["app"]["app_name"]} - {self.config["app"]["app_version"]}')

            for index, file in enumerate(self.files):
                print(index + 1, file[0])

        except Exception as e:
            print(f"Something went wrong: {e}")
