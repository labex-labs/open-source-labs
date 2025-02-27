# 推定器とパラメータグリッドを定義する

次に、調整したい推定器と検索したいパラメータグリッドを定義する必要があります。パラメータグリッドは、各ハイパーパラメータに対して試したい値を指定します。

```python
from sklearn.svm import SVC

# Create an instance of the support vector classifier
svc = SVC()

# Define the parameter grid
param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.1, 0.01, 0.001], 'kernel': ['linear', 'rbf']}
```
