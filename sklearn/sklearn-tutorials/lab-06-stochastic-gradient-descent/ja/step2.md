# データの読み込み

次に、scikit-learn からアヤメのデータセット（iris dataset）を読み込みます。このデータセットは、アヤメの花の測定値とそれに対応する種のラベルから構成される古典的な機械学習データセットです。

```python
iris = load_iris()
X = iris.data
y = iris.target
```
