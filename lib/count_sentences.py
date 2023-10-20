class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('The value must be a string.')

    def is_question(self):
        return self.value.endswith('The value must be a string?')

    def is_exclamation(self):
        return self.value.endswith('THe value must be a string!')

    def count_sentences(self):
        import re
        sentences = re.split(r'[.!?]+', self.value)
        non_empty_sentences = list(filter(lambda x: x.strip(), sentences))
        return len(non_empty_sentences)