# データの読み込み

scikit-learnのirisデータセットを使用します。このデータセットには150個のサンプルが含まれており、それぞれが4つの特徴量とターゲットラベルを持っています。

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
```
