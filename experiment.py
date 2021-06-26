from gensim.models.keyedvectors import KeyedVectors
import re

wv_embeddings = KeyedVectors.load_word2vec_format("SO_vectors_200.bin", binary=True)
for k in wv_embeddings.wv.index2word:
    with open("wv_emb_dict.txt", "a") as f:
        weights_text=str(wv_embeddings.wv[k])
        weights_text=re.sub(" ", ",", weights_text)
        try:
            f.write('"'+ k + '" : '+weights_text+',\n')
        except UnicodeEncodeError:
            pass


