class InvertedIndex:
    INVERTED_INDEX = {}

    def __init__(self, documents: list):
        self.__build(documents)

    def __build(self, documents: list):
        for index, document in enumerate(documents):
            self.add(index, document)

    def add(self, index: int, document: list):
        for word in document:
            if word in self.INVERTED_INDEX:
                if index in self.INVERTED_INDEX[word]:
                    self.INVERTED_INDEX[word]["count"] += 1
                else:
                    self.INVERTED_INDEX[word]["count"] = 1
            else:
                self.INVERTED_INDEX[word] = {"count": 1}

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
