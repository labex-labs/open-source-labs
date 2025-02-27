# データの読み込み

次に、機械学習において人気のある iris データセットを読み込みます。このデータセットには、さまざまな種類のアヤメの花の特徴に関する情報が含まれています。このデータセットを使って、K-Means クラスタリングアルゴリズムを示します。

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```
