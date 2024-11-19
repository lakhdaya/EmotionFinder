
SENTENCE = "Ainsi qu’un débauché pauvre qui baise et mange"
POEM = "poem.txt"

class Tokenizer:
    @staticmethod
    def replace(s: str) -> str:
        return s.replace(["...", "!", "?", ","], ' ').replace("\n", "").replace("'", " ")
    
    @staticmethod
    def create_vocab(s: str) -> set:
        s = Tokenizer.replace(s)
        vocab = set(s)
        return vocab

    def __init__(self, dataset: str) -> None:
        self.vocab = self.create_vocab(dataset)
        self.tokens = self.tokenize(dataset)

    def tokenize(self, sentence):
        None


def main():
    with open(POEM, 'r', encoding='UTF-8') as f:
        lines = f.read()
        tokenizer = Tokenizer(lines)
        print(tokenizer.vocab)


if __name__ == "__main__":
    main()