# Carregamento e Vectorização do Conjunto de Dados 20 Newsgroups

Definimos uma função para carregar dados do conjunto de dados 20newsgroups, que compreende cerca de 18.000 mensagens de grupos de notícias sobre 20 tópicos divididos em dois subconjuntos: um para treino e outro para teste. Carregaremos e vectorizaremos o conjunto de dados sem remover os metadados.

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
    """Carregar e vectorizar o conjunto de dados 20 newsgroups."""
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

    # a ordem das etiquetas em `target_names` pode ser diferente de `categories`
    target_names = data_train.target_names

    # dividir o alvo em um conjunto de treino e um conjunto de teste
    y_train, y_test = data_train.target, data_test.target

    # Extraindo características dos dados de treino usando um vectorizador esparso
    vectorizer = TfidfVectorizer(
        sublinear_tf=True, max_df=0.5, min_df=5, stop_words="english"
    )
    X_train = vectorizer.fit_transform(data_train.data)

    # Extraindo características dos dados de teste usando o mesmo vectorizador
    X_test = vectorizer.transform(data_test.data)

    feature_names = vectorizer.get_feature_names_out()

    if verbose:
        print(f"{len(data_train.data)} documentos")
        print(f"{len(data_test.data)} documentos")
        print(f"{len(target_names)} categorias")
        print(f"n_samples: {X_train.shape[0]}, n_features: {X_train.shape[1]}")
        print(f"n_samples: {X_test.shape[0]}, n_features: {X_test.shape[1]}")

    return X_train, X_test, y_train, y_test, feature_names, target_names

X_train, X_test, y_train, y_test, feature_names, target_names = load_dataset(verbose=True)
```
