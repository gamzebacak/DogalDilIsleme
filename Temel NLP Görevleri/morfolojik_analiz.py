import spacy

nlp = spacy.load("en_core_web_sm")

# incelenecek kelime
word = "books 123 the Ankara"

# kelimeyi nlp isleminden gecir
doc = nlp(word)

for token in doc:

    print("Text: ", token.text)  # dokümanın içindeki
    print("Lemma: ", token.lemma_)
    print("POS: ", token.pos_)  # sözcük türü
    print("Tag: ", token.tag_)
    print("Dependency: ", token.dep_)
    print("Shape: ", token.shape_)  #
    print("Is alpha: ", token.is_alpha)  # alfabatik mi
    print("Is stop: ", token.is_stop)
    print("Morphology: ", token.morph)  # morfolojik özellikleri
    print(f"Is plural: {'Number=Plur' in token.morph}")
    print(" ")
