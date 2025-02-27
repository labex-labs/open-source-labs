# データの読み込み

scikit-learnの乳がんデータセットを使用します。このデータセットには30の特徴と、患者が悪性または良性の癌を持っているかどうかを示す2値の目的変数があります。

```python
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
```
