class InvertedIndex:
    INVERTED_INDEX = {}

    def __init__(self, documents: list) -> None:
        self.__build(documents)

    def __build(self, documents: list) -> None:
        for index, document in enumerate(documents):
            self.add(index, document)

    def add(self, index: int, document: list) -> None:
        added_words = set()
        for position, word in enumerate(document):
            if word not in added_words:
                if word in self.INVERTED_INDEX:
                    self.INVERTED_INDEX[word]["count"] += 1
                    self.INVERTED_INDEX[word]["positions"].append(
                        [index, position])
                else:
                    self.INVERTED_INDEX[word] = {
                        "count": 1, "positions": [[index, position]]}
                added_words.add(word)

    def get(self) -> dict:
        return self.INVERTED_INDEX

    def find(self, word: str) -> dict:
        if word in self.INVERTED_INDEX:
            return self.INVERTED_INDEX[word]
        else:
            return {}

    def remove(self, word: str) -> bool:
        if word in self.INVERTED_INDEX:
            del self.INVERTED_INDEX[word]
            return True
        else:
            return False

    def clear(self) -> bool:
        try:
            self.INVERTED_INDEX = {}
            return True
        except Exception as e:
            print(e)
            return False

    def __len__(self) -> int:
        return len(self.INVERTED_INDEX)
