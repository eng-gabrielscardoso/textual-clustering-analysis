import configparser
import os
import sys


from src.app.inverted_index import InvertedIndex
from src.app.textual_analysis import TextualAnalysis
from src.utils.sanitisation import Sanitisation


class App:
    INI_FILE = "app.ini"
    ALLOWED_EXTENSIONS = (".txt")

    def __load_ini_file(self, filename) -> bool:
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

    def __load_files(self) -> bool:
        try:
            self.files = []
            full_path = os.path.abspath("./src/assets/texts")
            for filename in os.listdir(full_path):
                if filename.endswith(self.ALLOWED_EXTENSIONS):
                    file_path = os.path.join(full_path, filename)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        sanitised_content = Sanitisation.sanitise(content)
                        self.files.append(sanitised_content)

            return True
        except Exception as e:
            print(f"Failed to open words file: {e}")
            return False

    def __init__(self) -> None:
        if self.__load_ini_file(self.INI_FILE):
            if self.__load_files():
                self.__run()

    def __run(self) -> None:
        try:
            print(
                f'{self.config["app"]["app_name"]} - {self.config["app"]["app_version"]}')

            inverted_index = InvertedIndex(self.files)

            textual_analysis = TextualAnalysis(inverted_index, self.files)

            print(f'Abstract: {textual_analysis.search("abstract")}')
            print(f'Human: {textual_analysis.search("human")}')
            print(f'Clinical: {textual_analysis.search("clinical")}')
            textual_analysis.plot_common_words()
            textual_analysis.plot_clusters()
            textual_analysis.plot_search_time_comparison("abstract")
        except Exception as e:
            print(f"Something went wrong: {e}")
