# ラベル拡散モデル（Label Spreading Model）の訓練

gamma=0.25 と max_iter=20 でラベル拡散モデルを訓練します。

```python
lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
```
