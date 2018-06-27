# -*- coding: utf-8 -*-

from nltk.tokenize.api import TokenizerI
import spacy


class SpacyTokenizer(TokenizerI):
    """
    The Spacy tokenizer uses spaCy library to tokenize strings.

    """

    def tokenize(self, s):
        """
        Tokenizes string using spaCy library tokenizer.

        :param s: String to tokenize.
        :type s: str
        :return: str
        """
        nlp = spacy.load('en', disable=['tagger', 'parser', 'ner'])
        doc = nlp(s)
        return [w.text for w in doc]
