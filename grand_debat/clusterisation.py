import numpy as np


def apply_clusterisation(sentences_mixture_topics, topic_proba=0.7):
    """
    Filter to get the most characteristic sentences of each theme.

    Parameters
    ----------
    sentence_mixture_topics: np array
        Mixture of topics for each sentence
    topic_proba: float
        Keep only most relevant topics

    Returns
    -------
    sentences_paragraph: np array
    """
    sentences_paragraph = np.argmax(sentences_mixture_topics, axis=1)
    sentences_paragraph_proba = np.max(sentences_mixture_topics, axis=1)

    # filter
    sentences_paragraph = {i: x for i, x in enumerate(sentences_paragraph) if sentences_paragraph_proba[i]>topic_proba}

    return sentences_paragraph
