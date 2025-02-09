import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re
from collections import Counter

df = pd.read_csv("IMDB Dataset.csv")
df2 = df.head(100)

# metin verilerini alma
documents = df["review"]
labels = df["sentiment"]  # positive or negative

# metin temizleme fonksiyonu


def clean_text(text):
    # küçük harf çevrimi
    text = text.lower()

    # rakamları temizleme
    text = re.sub(r"\d+", "", text)

    # özel karakterleri temizleme
    text = re.sub(r"[^\w\s]", "", text)

    # kısa kelimeleri temizleme
    text = " ".join([word for word in text.split() if len(word) > 2])

    return text


# metinleri temizle
cleaned_documents = [clean_text(doc) for doc in documents]


# bow
vectorizer = CountVectorizer()

# metin -> sayısal vektör
X = vectorizer.fit_transform(cleaned_documents[:100])

# kelime kümesi
feature_names = vectorizer.get_feature_names_out()


# vektör temsili
print("Vektor Temsili")
vektor_temsili_2 = X.toarray()[:2]
print(vektor_temsili_2)

# vektor temsili dataframe
df_bow = pd.DataFrame(X.toarray(), columns=feature_names)

# kelime frekansı
word_counts = X.sum(axis=0).A1
word_freq = dict(zip(feature_names, word_counts))


# ilk 5 kelime
most_common_words = Counter(word_freq).most_common(5)
