# LabelPropagationを使ってラベルを学習する

未知のサンプルのラベルを学習するために、`LabelSpreading`を使います。

```python
label_spread = LabelSpreading(kernel="knn", alpha=0.8)
label_spread.fit(X, labels)
```
