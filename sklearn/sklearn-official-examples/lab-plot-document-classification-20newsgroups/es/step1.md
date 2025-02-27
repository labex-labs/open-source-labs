# Carga y vectorización del conjunto de datos de texto 20 Newsgroups

Definimos una función para cargar datos del conjunto de datos 20newsgroups_dataset, que comprende alrededor de 18.000 publicaciones de grupos de noticias sobre 20 temas divididas en dos subconjuntos: uno para entrenamiento y el otro para prueba. Cargaremos y vectorizaremos el conjunto de datos sin eliminar los metadatos.

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
    """Carga y vectoriza el conjunto de datos 20 newsgroups."""
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

    # El orden de las etiquetas en `target_names` puede ser diferente de `categories`
    target_names = data_train.target_names

    # Divide la variable objetivo en un conjunto de entrenamiento y un conjunto de prueba
    y_train, y_test = data_train.target, data_test.target

    # Extracción de características a partir de los datos de entrenamiento utilizando un vectorizador disperso
    vectorizer = TfidfVectorizer(
        sublinear_tf=True, max_df=0.5, min_df=5, stop_words="english"
    )
    X_train = vectorizer.fit_transform(data_train.data)

    # Extracción de características a partir de los datos de prueba utilizando el mismo vectorizador
    X_test = vectorizer.transform(data_test.data)

    feature_names = vectorizer.get_feature_names_out()

    if verbose:
        print(f"{len(data_train.data)} documentos")
        print(f"{len(data_test.data)} documentos")
        print(f"{len(target_names)} categorías")
        print(f"n_samples: {X_train.shape[0]}, n_features: {X_train.shape[1]}")
        print(f"n_samples: {X_test.shape[0]}, n_features: {X_test.shape[1]}")

    return X_train, X_test, y_train, y_test, feature_names, target_names

X_train, X_test, y_train, y_test, feature_names, target_names = load_dataset(verbose=True)
```
