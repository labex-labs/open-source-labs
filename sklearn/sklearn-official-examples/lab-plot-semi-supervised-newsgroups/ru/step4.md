# Создание конвейера (pipeline) для Self-Training

На этом шаге мы создадим конвейер (pipeline) для полусupervised обучения с использованием метода Self-Training. Конвейер будет аналогичен конвейеру для supervised обучения, но вместо SGDClassifier мы будем использовать SelfTrainingClassifier.

```python
from sklearn.semi_supervised import SelfTrainingClassifier

# Создание конвейера (pipeline) для Self-Training
st_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SelfTrainingClassifier(SGDClassifier(**sdg_params), verbose=True)),
    ]
)
```
