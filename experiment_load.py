from gensim.models.keyedvectors import Word2VecKeyedVectors
import json
import numpy as np
with open('wv_emb_dict.json') as json_data:
    d = json.loads(json_data)
    json_data.close()
wv_embeddings = Word2VecKeyedVectors(vector_size=200)
wv_embeddings.vocab = d
wv_embeddings.vectors = np.array(list(d.values()))
word = 'cat'
if word in wv_embeddings:
    print(wv_embeddings[word].dtype, wv_embeddings[word].shape)
