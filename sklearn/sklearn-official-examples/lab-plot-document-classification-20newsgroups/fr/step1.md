# Chargement et vectorisation de l'ensemble de données texte 20 Newsgroups

Nous définissons une fonction pour charger les données à partir de l'ensemble de données 20newsgroups_dataset, qui comprend environ 18 000 messages de newsgroup sur 20 sujets divisés en deux sous-ensembles : l'un pour l'entraînement et l'autre pour le test. Nous allons charger et vectoriser l'ensemble de données sans élimination des métadonnées.

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
    """Charge et vectorise l'ensemble de données 20 newsgroups."""
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

    # L'ordre des étiquettes dans `target_names` peut être différent de `categories`
    target_names = data_train.target_names

    # Diviser la cible en un ensemble d'entraînement et un ensemble de test
    y_train, y_test = data_train.target, data_test.target

    # Extraction des caractéristiques à partir des données d'entraînement en utilisant un vectoriseur creux
    vectorizer = TfidfVectorizer(
        sublinear_tf=True, max_df=0.5, min_df=5, stop_words="english"
    )
    X_train = vectorizer.fit_transform(data_train.data)

    # Extraction des caractéristiques à partir des données de test en utilisant le même vectoriseur
    X_test = vectorizer.transform(data_test.data)

    feature_names = vectorizer.get_feature_names_out()

    if verbose:
        print(f"{len(data_train.data)} documents")
        print(f"{len(data_test.data)} documents")
        print(f"{len(target_names)} catégories")
        print(f"n_samples: {X_train.shape[0]}, n_features: {X_train.shape[1]}")
        print(f"n_samples: {X_test.shape[0]}, n_features: {X_test.shape[1]}")

    return X_train, X_test, y_train, y_test, feature_names, target_names

X_train, X_test, y_train, y_test, feature_names, target_names = load_dataset(verbose=True)
```
