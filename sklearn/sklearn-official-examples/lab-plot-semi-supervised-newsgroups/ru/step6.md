# Создание конвейера (pipeline) для LabelSpreading

На этом шаге мы создадим конвейер (pipeline) для полусupervised обучения с использованием алгоритма LabelSpreading. Конвейер будет аналогичен конвейеру для supervised обучения, но вместо SGDClassifier мы будем использовать алгоритм LabelSpreading.

```python
from sklearn.semi_supervised import LabelSpreading
from sklearn.preprocessing import FunctionTransformer

# Создание конвейера (pipeline) LabelSpreading
ls_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("toarray", FunctionTransformer(lambda x: x.toarray())),
        ("clf", LabelSpreading()),
    ]
)
```
