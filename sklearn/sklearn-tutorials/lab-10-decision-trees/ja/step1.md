# 必要なライブラリをインポートする

まず、必要なライブラリをインポートする必要があります。決定木（Decision Tree）分類器を構築して訓練するために、scikit-learn を使用します。

```python
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```
