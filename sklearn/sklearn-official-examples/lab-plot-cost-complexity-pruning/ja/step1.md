# データの読み込み

scikit-learn の乳がんデータセットを使用します。このデータセットには 30 の特徴と、患者が悪性または良性の癌を持っているかどうかを示す 2 値の目的変数があります。

```python
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
```
