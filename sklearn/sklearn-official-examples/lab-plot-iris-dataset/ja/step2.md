# Iris データセットの読み込み

Scikit-learn の組み込み関数 `load_iris` を使って Iris データセットを読み込みます。

```python
iris = datasets.load_iris()
X = iris.data[:, :2]  # 最初の 2 つの特徴のみを取ります。
y = iris.target
```
