# データセットの理解

Scikit-learn は、データセットを 2 次元配列として表現します。ここで、最初の軸はサンプルを表し、2 番目の軸は特徴量を表します。iris データセットを使った例を見てみましょう。

```python
from sklearn import datasets

iris = datasets.load_iris()
data = iris.data
print(data.shape)
```

出力：

```
(150, 4)
```

iris データセットは、150 個のアヤメの観測値で構成されており、各観測値は 4 つの特徴量で記述されています。データ配列の形状は (150, 4) です。
