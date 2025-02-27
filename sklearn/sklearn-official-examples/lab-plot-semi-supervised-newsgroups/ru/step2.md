# Создание конвейера (pipeline) для supervised обучения

На этом шаге мы создадим конвейер (pipeline) для supervised обучения. Конвейер будет состоять из CountVectorizer, который преобразует текстовые данные в матрицу подсчета токенов, TfidfTransformer, который применяет нормализацию частоты термина - обратной частоты документа (term frequency - inverse document frequency) к матрице подсчета, и SGDClassifier, который обучает модель.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

# Параметры для SGDClassifier
sdg_params = dict(alpha=1e-5, penalty="l2", loss="log_loss")

# Параметры для CountVectorizer
vectorizer_params = dict(ngram_range=(1, 2), min_df=5, max_df=0.8)

# Создание конвейера (pipeline)
pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SGDClassifier(**sdg_params)),
    ]
)
```
