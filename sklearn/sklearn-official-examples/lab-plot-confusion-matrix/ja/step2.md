# データの読み込み

scikit-learn の iris データセットを使用します。このデータセットには 150 個のサンプルが含まれており、それぞれが 4 つの特徴量とターゲットラベルを持っています。

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
```
