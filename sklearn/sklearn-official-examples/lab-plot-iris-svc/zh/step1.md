# 导入必要的库并加载数据集

```python
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.inspection import DecisionBoundaryDisplay

# 导入一些数据用于实验
iris = datasets.load_iris()
# 取前两个特征。我们可以通过使用二维数据集来避免这一步
X = iris.data[:, :2]
y = iris.target
```
