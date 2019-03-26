from nltk.tokenize import sent_tokenize
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx


def prepare_data(data_theme_response_dict, selected_question):
    """
    Separate data into clean sentences

    Parameters
    ----------
    data_theme_response_dict: {}
        Responses associated to a question
    selected_question: str
        Question to study

    Returns
    -------
    clean_sentences: [str]
        Cleaned sentences
    """
    # split the the text in the articles into sentences
    sentences = []
    for s in data_theme_response_dict[selected_question]:
        sentences.append(sent_tokenize(s))

    # flatten the list
    sentences = [y for x in sentences for y in x]

    # remove punctuations, numbers and special characters
    clean_sentences = pd.Series(sentences).str.replace(" ", " ")

    # make alphabets lowercase
    clean_sentences = [s.lower() for s in clean_sentences]

    return clean_sentences


def create_titles(clean_sentences, tf_vectorizer, lda_tf):
    """
    Applies clustering algorithm in order to get most characteristic themes

    Parameters
    ----------
    clean_sentences: [str]
        Answers to a question
    tf_vectorizer: sklearn object
        Vectorizer
    lda_tf: sklearn object
        LDA fitted
    """
    title_sentences = [x for x in clean_sentences if len(x) < 250]
    title_sentences = [x for x in title_sentences if "\n" not in x]
    sentence_tf = tf_vectorizer.transform(title_sentences)
    sentences_mixture_topics = lda_tf.transform(sentence_tf)
    titles = np.argmax(sentences_mixture_topics, axis=0)
    for t in [title_sentences[x] for x in titles]:
        print(t, '\n')
    return sentences_mixture_topics, title_sentences, titles


def apply_page_rank_algorithm(clean_sentences, sentences_paragraph, word_embeddings, sn):
    """
    Apply the page rank algorithm over the sentence graph to get the
    text summarization
    """
    sentences_summary = [x for i, x in enumerate(clean_sentences) if sentences_paragraph.get(i, -1)==1]
    sentences_summary_emb = []
    for i in sentences_summary:
        if len(i) != 0:
            v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
        else:
            v = np.zeros((100,))
        sentences_summary_emb.append(v)
    sim_mat = cosine_similarity(sentences_summary_emb)
    nx_graph = nx.from_numpy_array(sim_mat)
    try:
        scores = nx.pagerank(nx_graph)
    except:
        scores = nx.pagerank_numpy(nx_graph)
    ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences_summary)), reverse=True)
    for i in range(sn):
        print('•', ranked_sentences[i][1], '\n')
