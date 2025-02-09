from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "Kedi evde",
    "Kedi bahçede"]

vectorizer = CountVectorizer()

# metin-> sayısal vektör

X = vectorizer.fit_transform(documents)

# Kelime kümesi ["Kedi" , "evde" , "bahçede"]
print("Kelime Kümesi: ", vectorizer.get_feature_names_out())

# vektör temsili
print("Vektör temsili: ", X.toarray())
