# データの読み込み

このステップでは、scikit-learn の datasets モジュールを使って iris データセットを読み込みます。データセットの最初の 2 つの特徴量を選択して変数 X に割り当てます。また、目的変数を Y に割り当てます。

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
Y = iris.target
```
