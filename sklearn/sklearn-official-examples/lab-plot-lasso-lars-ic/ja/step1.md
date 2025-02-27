# データの読み込み

scikit-learnからload_diabetesメソッドを使って糖尿病データセットを読み込みます。

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
```
