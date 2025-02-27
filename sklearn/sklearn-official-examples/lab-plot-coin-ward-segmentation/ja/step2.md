# データの構造を定義する

画像内の画素はその近傍の画素と接続されています。画像に対して階層的クラスタリングを行うためには、データの構造を定義する必要があります。データの構造を定義する接続行列を作成するために、scikit-learnの`grid_to_graph`関数を使うことができます。

```python
from sklearn.feature_extraction.image import grid_to_graph

connectivity = grid_to_graph(*rescaled_coins.shape)
```
