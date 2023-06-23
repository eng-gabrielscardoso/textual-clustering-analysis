import configparser
import logging
import os
import sys


class App:
    INI_FILE = "app.ini"

    def __load_ini_file(self, filename):
        full_path = os.path.abspath(os.path.join("./src", filename))
        path_config_file = full_path if os.path.isfile(full_path) else \
            os.path.abspath(os.path.join(
                os.path.dirname(sys.executable), filename))
        self.config = configparser.ConfigParser()
        if self.config.read(path_config_file):
            return True
        else:
            logging.basicConfig(
                level=logging.ERROR,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                filename='logs/app.log',
                filemode='w',
            )
            logging.error(f"Couldn't load file in {path_config_file}")
            return False

    def __load_file(self, filenames):
        try:
            self.words = []
            for filename in filenames:
                full_path = os.path.abspath(
                    os.path.join("./src/assets/texts", filename))
                path_words_file = full_path if os.path.isfile(full_path) else \
                    os.path.abspath(os.path.join(
                        os.path.dirname(sys.executable), filename))
                with open(path_words_file, 'r', encoding='utf-8') as file:
                    first_word = file.readline().split()[0]
                    self.words.append(first_word)
            return True
        except Exception as e:
            logging.error(f"Failed to open words file: {e}", exc_info=True)
            return False

    def __init__(self) -> None:
        if self.__load_ini_file(self.INI_FILE):
            words_files = self.config.get("assets", "words_files").split(",")
            if self.__load_file(words_files):
                self.__run()

    def __run(self):
        try:
            print(
                f'{self.config["app"]["app_name"]} - {self.config["app"]["app_version"]}')
            for index, word in enumerate(self.words):
                print(f'{"0{}".format(index) if index < 10 else index + 1} - {word}')
        except Exception as e:
            logging.error(f"Something went wrong: {e}")
        finally:
            if self.words:
                self.words.close()
