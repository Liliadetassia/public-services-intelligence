import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

CATEGORIES = ["Saúde", "Educação", "Assistência Social"]

def train():
    data = {
        "text": [
            "falta médico no posto",
            "fila grande na unidade de saúde",
            "escola sem professor",
            "problemas na creche",
            "demora no atendimento do cras",
            "benefício social atrasado"
        ],
        "label": [
            "Saúde",
            "Saúde",
            "Educação",
            "Educação",
            "Assistência Social",
            "Assistência Social"
        ]
    }

    df = pd.DataFrame(data)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["text"])

    model = MultinomialNB()
    model.fit(X, df["label"])

    return model, vectorizer


def predict(text, model, vectorizer):
    X = vectorizer.transform([text])
    return model.predict(X)[0]
