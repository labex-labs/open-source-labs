# データセットの読み込みと前処理

scikit-learn ライブラリを使ってアヤメデータセットを読み込みます。このデータセットは、それぞれ 50 個のインスタンスからなる 3 つのクラスが含まれており、各クラスはある種のアヤメ植物を指します。各インスタンスは 4 つの特徴量を持っています。がく片の長さ、がく片の幅、花びらの長さ、花びらの幅。

```python
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay

# アヤメデータセットを読み込む
iris = datasets.load_iris()
X = iris.data[:, :2]  # 最初の 2 つの特徴量のみを取り出します。
Y = iris.target
```
