# データセットを読み込む

次に、Scikit-learn から iris データセットを読み込みます。

```python
iris = datasets.load_iris()
X = iris.data[:, 0:2]  # 可視化のため、最初の 2 つの特徴のみを使用します
y = iris.target
n_features = X.shape[1]
```
