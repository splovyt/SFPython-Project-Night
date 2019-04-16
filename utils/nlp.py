import ssl

import nltk
from textblob import TextBlob
from nltk.corpus import stopwords


# set SSL
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# download noun data (if required)
nltk.download('brown')
nltk.download('punkt')
nltk.download('stopwords')

def extract_nouns(sentence):
    """Extract the nouns from a sentence using the 'textblob' library."""
    blob = TextBlob(sentence)
    return blob.noun_phrases

def remove_stopwords(sentence):
    """Remove stopwords from a sentence and return the list of words."""
    blob = TextBlob(sentence)
    return [word for word in blob.words if word not in stopwords.words('english') and len(word)>2]
