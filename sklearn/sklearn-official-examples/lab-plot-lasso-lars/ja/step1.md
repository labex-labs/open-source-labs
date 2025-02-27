# データの読み込み

最初のステップは、Scikit-Learnから糖尿病データセットを読み込むことです。

```python
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
```
