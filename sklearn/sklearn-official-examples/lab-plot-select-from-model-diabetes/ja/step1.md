# データの読み込み

私たちは scikit - learn から糖尿病データセットを読み込み、その説明を表示します。

```python
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
print(diabetes.DESCR)
```
