# Загрузка и векторизация текстового датасета 20 Newsgroups

Мы определяем функцию для загрузки данных из датасета 20newsgroups_dataset, который содержит около 18 000 новостных сообщений по 20 темам, разделенных на две подмножества: одно для обучения, а другое для тестирования. Мы будем загружать и векторизовать датасет без удаления метаданных.

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
    """Загрузка и векторизация датасета 20 newsgroups."""
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

    # порядок меток в `target_names` может отличаться от `categories`
    target_names = data_train.target_names

    # разделение целевого признака на тренировочный и тестовый наборы
    y_train, y_test = data_train.target, data_test.target

    # Извлечение признаков из тренировочных данных с использованием разреженного векторизатора
    vectorizer = TfidfVectorizer(
        sublinear_tf=True, max_df=0.5, min_df=5, stop_words="english"
    )
    X_train = vectorizer.fit_transform(data_train.data)

    # Извлечение признаков из тестовых данных с использованием того же векторизатора
    X_test = vectorizer.transform(data_test.data)

    feature_names = vectorizer.get_feature_names_out()

    if verbose:
        print(f"{len(data_train.data)} документов")
        print(f"{len(data_test.data)} документов")
        print(f"{len(target_names)} категорий")
        print(f"n_samples: {X_train.shape[0]}, n_features: {X_train.shape[1]}")
        print(f"n_samples: {X_test.shape[0]}, n_features: {X_test.shape[1]}")

    return X_train, X_test, y_train, y_test, feature_names, target_names

X_train, X_test, y_train, y_test, feature_names, target_names = load_dataset(verbose=True)
```
