# Laden und Vektorisieren des 20 Newsgroups Text-Datensatzes

Wir definieren eine Funktion, um Daten aus dem 20newsgroups-Datensatz zu laden, der ungefähr 18.000 Newsgroup-Beiträge zu 20 Themen enthält, die in zwei Teilmengen unterteilt sind: eine für das Training und die andere für das Testen. Wir werden den Datensatz laden und vektorisieren, ohne die Metadaten zu entfernen.

```python
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

categories = [
    "alt.atheism",
    "talk.religion.misc",
    "comp.graphics",
    "sci.space",
]

def load_dataset(verbose=False, remove=()):
    """Laden und Vektorisieren des 20 Newsgroups-Datensatzes."""
    data_train = fetch_20newsgroups(
        subset="train",
        categories=categories,
        shuffle=True,
        random_state=42,
        remove=remove,
    )

    data_test = fetch_20newsgroups(
        subset="test",
        categories=categories,
        shuffle=True,
        random_state=42,
        remove=remove,
    )

    # Die Reihenfolge der Labels in `target_names` kann von `categories` unterschiedlich sein
    target_names = data_train.target_names

    # Teilen Sie das Ziel in einen Trainingssatz und einen Testsatz auf
    y_train, y_test = data_train.target, data_test.target

    # Extrahieren von Merkmalen aus den Trainingsdaten mit einem sparsen Vektorizer
    vectorizer = TfidfVectorizer(
        sublinear_tf=True, max_df=0.5, min_df=5, stop_words="english"
    )
    X_train = vectorizer.fit_transform(data_train.data)

    # Extrahieren von Merkmalen aus den Testdaten mit dem gleichen Vektorizer
    X_test = vectorizer.transform(data_test.data)

    feature_names = vectorizer.get_feature_names_out()

    if verbose:
        print(f"{len(data_train.data)} Dokumente")
        print(f"{len(data_test.data)} Dokumente")
        print(f"{len(target_names)} Kategorien")
        print(f"n_samples: {X_train.shape[0]}, n_features: {X_train.shape[1]}")
        print(f"n_samples: {X_test.shape[0]}, n_features: {X_test.shape[1]}")

    return X_train, X_test, y_train, y_test, feature_names, target_names

X_train, X_test, y_train, y_test, feature_names, target_names = load_dataset(verbose=True)
```
