#!/usr/bin/env python3
import re


class MyString:

    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, assigned_value):
        if not isinstance(assigned_value, str):
            print("The value must be a string.")
        self._value = assigned_value

    def is_sentence(self):
        return True if self._value.endswith(".") else False

    def is_question(self):
        return True if self._value.endswith("?") else False

    def is_exclamation(self):
        return True if self._value.endswith("!") else False

    def count_sentences(self):
        return len(
            [sentence for sentence in re.split(r"[.!?]", self._value) if sentence]
        )


sentences = MyString()
sentences.value = "This is a string! It has three sentences. Right?"
print(sentences.count_sentences())
