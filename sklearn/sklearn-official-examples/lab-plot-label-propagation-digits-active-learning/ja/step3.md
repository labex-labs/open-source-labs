# ラベル伝播モデルを学習する

ここで、ラベル付きのデータポイントを使ってラベル伝播モデルを学習し、残りの非ラベル付きのデータポイントのラベルを予測するために使います。

```python
from sklearn.semi_supervised import LabelSpreading

lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
predicted_labels = lp_model.transduction_[unlabeled_indices]
```
