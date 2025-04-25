# データを読み込む

次に、Scikit-learn から iris データセットを読み込み、可視化の目的で最初の 2 つの特徴のみを選択します。

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target
```
