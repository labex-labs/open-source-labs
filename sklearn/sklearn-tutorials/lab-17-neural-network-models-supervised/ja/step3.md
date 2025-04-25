# MLP モデルを作成して学習する

```python
# 5 つのニューロンからなる 1 つの隠れ層を持つ MLP 分類器を作成する
clf = MLPClassifier(hidden_layer_sizes=(5,), random_state=1)

# 学習データを使ってモデルを学習する
clf.fit(X, y)
```
