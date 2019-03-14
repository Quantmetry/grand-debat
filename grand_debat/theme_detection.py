import pyLDAvis
import pyLDAvis.sklearn
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.simplefilter('ignore')
pyLDAvis.enable_notebook()


def get_themes(data_theme_response_dict, selected_question, n_topics=20, max_iter=100):
    """
    Get the main themes of selected question and save them in the following
    file: pyLDAVIS_tf.html
    """
    tf_vectorizer = CountVectorizer(min_df=5, max_df=0.9)
    dtm_tf = tf_vectorizer.fit_transform(data_theme_response_dict[selected_question])

    lda_tf = LatentDirichletAllocation(n_topics=n_topics, random_state=0, n_jobs=-1, verbose=1, max_iter=max_iter, perp_tol=0.5, evaluate_every=4)
    lda_tf.fit(dtm_tf)

    pyLDAVIS_tf = pyLDAvis.sklearn.prepare(lda_tf, dtm_tf, tf_vectorizer)
    pyLDAvis.save_html(pyLDAVIS_tf, 'pyLDAVIS_tf.html')

    return tf_vectorizer, lda_tf
