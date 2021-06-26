from db_help import *
import logging
from typing import List, Union
from gensim.models.keyedvectors import KeyedVectors
import numpy as np
from nltk.tokenize import WordPunctTokenizer
from sklearn.metrics.pairwise import cosine_similarity


class SimCosModel():
    def __init__(self, weights_path="SO_vectors_200.bin"):
        self.embeddings = KeyedVectors.load_word2vec_format(weights_path, binary=True)
        self.tokenizer = WordPunctTokenizer()
        logging.info("Models are initialized now")

    def text_to_vec(self, text_string: str, dim=200) -> np.ndarray:
        text_string = text_string.lower()
        tokens = self.tokenizer.tokenize(text_string)
        relevant = 0
        words_vecs = np.zeros((dim,))
        for word in tokens:
            if word in self.embeddings:
                words_vecs += self.embeddings[word]
                relevant += 1

        if relevant:
            words_vecs /= relevant
        return words_vecs.reshape(1, -1)

    def rang_candidates_strings(self, request_to_fit: str, candidates: List[str], dim=200) -> List[str]:
        question_vec = self.text_to_vec(request_to_fit)
        candidates.sort(key=lambda candidate: -cosine_similarity(question_vec, self.text_to_vec(candidate)))
        return candidates

    def rang_candidates(self, request_to_fit: Union[About, Vacancy], candidates: List[Union[About, Vacancy]],
                        dim=200) -> List[int]:
        question_vec = self.text_to_vec(request_to_fit.description)
        candidates.sort(key=lambda candidate: -cosine_similarity(question_vec, self.text_to_vec(candidate.description)))
        return [candidate.id for candidate in candidates]

    def similarity(self, text1: str, text2: str) -> float:
        text1_vec = self.text_to_vec(text1)
        text2_vec = self.text_to_vec(text2)
        return cosine_similarity(text1_vec, text2_vec)[0][0]


class Predictor():
    def __init__(self, weights_path="SO_vectors_200.bin"):
        self.embeddings = KeyedVectors.load_word2vec_format(weights_path, binary=True)

    async def word_coo(self, word: str) -> Union[np.ndarray, bool]:
        if word in self.embeddings:
            return self.embeddings[word]
        else:
            return False
