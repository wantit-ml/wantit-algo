from gensim.models.keyedvectors import KeyedVectors
from db_embedding import *

wv_embeddings = KeyedVectors.load_word2vec_format("SO_vectors_200.bin", binary=True)
for k in wv_embeddings.wv.index2word:
    weights_text=str(wv_embeddings.wv[k].tolist())
    weights_text=weights_text[1:-1]
    new_vector = Vector(word=k, coords=weights_text)
    vectors_db.add(new_vector)
    vectors_db.commit()




