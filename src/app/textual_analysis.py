import time
import matplotlib.pyplot as plt
from src.app.huffman_algorithm import HuffmanAlgorithm


class TextualAnalysis:
    def __init__(self, invertedIndexes, rawFiles):
        self.INVERTED_INDEXES = invertedIndexes.get()
        self.RAW_FILES = rawFiles
        self.COMPRESSED_TEXTS = self.compress_texts()

    def common_words(self):
        common_words = []

        if len(self.INVERTED_INDEXES) > 0:
            for word, data in self.INVERTED_INDEXES.items():
                count = data["count"]
                positions = [entry[0] for entry in data["positions"]]
                common_words.append([word, count, positions])

        return common_words

    def compress_texts(self):
        compressed_texts = []

        if len(self.RAW_FILES) > 0:
            huffman_coding = HuffmanAlgorithm()
            frequencies = self.calculate_frequencies()
            huffman_tree = huffman_coding.build_huffman_tree(frequencies)
            huffman_coding.build_huffman_codes(huffman_tree)
            self.HUFFMAN_TREE = huffman_tree
            self.HUFFMAN_CODES = huffman_coding.codes

            for document in self.RAW_FILES:
                compressed_text = huffman_coding.compress_text(document)
                compressed_texts.append(compressed_text)

        return compressed_texts

    def calculate_frequencies(self):
        frequencies = {}

        for document in self.RAW_FILES:
            for word in document:
                if word in frequencies:
                    frequencies[word] += 1
                else:
                    frequencies[word] = 1

        return frequencies

    def search(self, word):
        documents = []

        if len(self.RAW_FILES) > 0 and word in self.RAW_FILES[0]:
            for index, document in enumerate(self.RAW_FILES):
                if word in document:
                    documents.extend(
                        [(index, pos) for pos, w in enumerate(document) if w == word])

        return documents

    def compare_search_time(self, word):
        search_time = {}

        start_time = time.time()
        self.search(word)
        end_time = time.time()
        search_time['uncompressed'] = end_time - start_time

        compressed_texts = self.compress_texts()

        start_time = time.time()
        self.search_in_compressed(word, compressed_texts)
        end_time = time.time()
        search_time['compressed'] = end_time - start_time

        return search_time

    def search_in_compressed(self, word, compressed_texts):
        documents = []

        for index, compressed_text in enumerate(compressed_texts):
            decoded_text = self.decode_text(compressed_text)
            positions = [i for i, w in enumerate(decoded_text) if w == word]

            if positions:
                documents.extend([(index, pos) for pos in positions])

        return documents

    def decode_text(self, compressed_text):
        decoded_text = ''
        current_code = ''
        index = 0
        huffman_codes_reversed = {
            code: word for word,
            code in self.HUFFMAN_CODES.items()}

        while index < len(compressed_text):
            current_code += compressed_text[index]

            if current_code in huffman_codes_reversed:
                decoded_text += huffman_codes_reversed[current_code]
                current_code = ''

            index += 1

        return decoded_text

    def plot_common_words(self, limit: int = 20):
        common_words = self.common_words()
        common_words.sort(key=lambda x: x[1], reverse=True)
        words = [word[0] for word in common_words[:limit]]
        counts = [word[1] for word in common_words[:limit]]

        plt.bar(words, counts)
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.title('Most Common Words')
        plt.xticks(rotation=90)
        plt.show()

    def plot_clusters(self):
        common_words = self.common_words()
        common_words.sort(key=lambda x: x[1], reverse=True)

        files = []
        most_common_words = []

        for index in range(len(self.RAW_FILES)):
            words_in_file = []
            for word_info in common_words:
                word = word_info[0]
                positions = word_info[2]
                if index in positions:
                    words_in_file.append(word)
            if words_in_file:
                most_common_word = max(
                    set(words_in_file), key=words_in_file.count)
                files.append(f"Text {index + 1}")
                most_common_words.append(most_common_word)

        plt.bar(files, most_common_words)
        plt.xlabel('Files')
        plt.ylabel('Most Common Word')
        plt.title('Most Common Word in Each File')
        plt.xticks(rotation=90)
        plt.show()

    def plot_search_time_comparison(self, word):
        search_time = self.compare_search_time(word)

        plt.bar(list(search_time.keys()), list(search_time.values()))
        plt.xlabel('Index Type')
        plt.ylabel('Search Time')
        plt.title('Search Time Comparison')
        plt.show()
