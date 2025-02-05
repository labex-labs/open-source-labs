# 创建标签传播管道

在这一步中，我们将创建一个使用标签传播的半监督学习管道。该管道将与监督管道类似，但我们将使用标签传播算法代替SGDClassifier。

```python
from sklearn.semi_supervised import LabelSpreading
from sklearn.preprocessing import FunctionTransformer

# 创建标签传播管道
ls_pipeline = Pipeline(
    [
        ("vect", CountVectorizer(**vectorizer_params)),
        ("tfidf", TfidfTransformer()),
        ("toarray", FunctionTransformer(lambda x: x.toarray())),
        ("clf", LabelSpreading()),
    ]
)
```
