# SVMによる分類

- 必要なライブラリをインポートして始めましょう：

```python
from sklearn import svm
```

- 学習サンプル `X` とクラスラベル `y` を定義します：

```python
X = [[0, 0], [1, 1]]
y = [0, 1]
```

- `SVC` 分類器のインスタンスを作成し、データにフィットさせます：

```python
clf = svm.SVC()
clf.fit(X, y)
```

- 学習済みモデルを使って新しい値を予測します：

```python
clf.predict([[2., 2.]])
```
