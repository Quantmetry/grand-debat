import numpy as np


def sentence_to_vec(clean_sentences, file_model='data/word2vec.10k.100d.txt'):
    """
    Use pretrained word2vec model and represent each sentence by a vector.

    Parameters
    ----------
    clean_sentences: [str]
        Answers
    file_model: str
        Word vectors file

    Returns
    -------
    sentence_vectors: [[float]]
        Dense representations
    word_embeddings: [[float]]
        Word embeddings
    """
    # Extract word vectors
    word_embeddings = {}
    f = open(file_model, encoding='utf-8')
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        word_embeddings[word] = coefs
    f.close()

    sentence_vectors = []
    for i in clean_sentences:
        if len(i) != 0:
            v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()]) / (len(i.split())+0.001)
        else:
            v = np.zeros((100,))
        sentence_vectors.append(v)

    return sentence_vectors, word_embeddings
