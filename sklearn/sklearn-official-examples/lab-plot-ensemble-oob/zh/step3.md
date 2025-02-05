# 定义集成分类器

我们将定义一个包含三个随机森林分类器的列表，每个分类器的 `max_features` 参数都有不同的值。我们会将 `warm_start` 构造参数设置为 `True`，以便在训练期间跟踪袋外（OOB）错误率。我们还会将 `oob_score` 参数设置为 `True`，以启用 OOB 错误率计算。

```python
ensemble_clfs = [
    (
        "RandomForestClassifier, max_features='sqrt'",
        RandomForestClassifier(
            warm_start=True,
            oob_score=True,
            max_features="sqrt",
            random_state=RANDOM_STATE,
        ),
    ),
    (
        "RandomForestClassifier, max_features='log2'",
        RandomForestClassifier(
            warm_start=True,
            max_features="log2",
            oob_score=True,
            random_state=RANDOM_STATE,
        ),
    ),
    (
        "RandomForestClassifier, max_features=None",
        RandomForestClassifier(
            warm_start=True,
            max_features=None,
            oob_score=True,
            random_state=RANDOM_STATE,
        ),
    ),
]
```
