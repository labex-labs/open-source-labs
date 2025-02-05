# 创建自训练管道

在这一步中，我们将创建一个使用自训练的半监督学习管道。该管道将与监督管道类似，但我们将使用SelfTrainingClassifier而不是SGDClassifier。

```python
from sklearn.semi_supervised import SelfTrainingClassifier

# 创建自训练管道
st_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("clf", SelfTrainingClassifier(SGDClassifier(**sdg_params), verbose=True)),
    ]
)
```
