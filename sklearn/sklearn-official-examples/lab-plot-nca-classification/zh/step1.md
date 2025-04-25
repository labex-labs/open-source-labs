# 导入库

我们将首先导入必要的库。我们将使用 scikit-learn 来执行最近邻分类和 NCA。我们将使用 matplotlib 来绘制类别决策边界。

```python
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis
from sklearn.pipeline import Pipeline
from sklearn.inspection import DecisionBoundaryDisplay
```
