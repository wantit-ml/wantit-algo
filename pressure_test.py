import tracemalloc
from gensim.models.keyedvectors import KeyedVectors
import re
import time

tracemalloc.start()
wv_embeddings = KeyedVectors.load_word2vec_format("SO_vectors_200.bin", binary=True)
snapshot = tracemalloc.take_snapshot()
for line in snapshot.statistics("lineno"):
    print(line)
time.sleep(100)

