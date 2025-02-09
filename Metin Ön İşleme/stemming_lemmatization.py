from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import nltk
nltk.download("wordnet")


stemmer = PorterStemmer()

# ornek kelimeler
words = ["running", "runner", "ran", "runs", "better", "go", "went"]

stems = [stemmer.stem(w) for w in words]

print("Stem result: ", stems)

# %% lemma


lemmatizer = WordNetLemmatizer()

# ornek kelimeler
words = ["running", "runner", "ran", "runs", "better", "go", "went"]

lemmas = [lemmatizer.lemmatize(w, pos="v") for w in words]

print("Lemma result: ", lemmas)
