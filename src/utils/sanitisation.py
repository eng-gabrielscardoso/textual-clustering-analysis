class Sanitisation:

    def __init__(self) -> None:
        pass

    @staticmethod
    def sanitise(file: str) -> list[str]:
        try:
            sanitised_file = []
            words = file.split()
            for word in words:
                sanitised_word = ''.join(c.lower()
                                         for c in word if c.isalnum())
                if sanitised_word:
                    sanitised_file.append(sanitised_word)

            if (len(sanitised_file) == 0 and sanitised_file[0] == ''):
                return []

            return sanitised_file
        except Exception as e:
            print(e)
            return []
