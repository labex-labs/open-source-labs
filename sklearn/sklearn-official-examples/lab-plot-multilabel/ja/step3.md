# データセットの生成

このステップでは、`sklearn.datasets` からの `make_multilabel_classification` 関数を使ってデータセットを生成します。

```python
X, Y = make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=True, random_state=1
)
```
