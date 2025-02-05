# 导入数据集

第一步是导入我们将使用的数据集。

```python
# 导入pandas库
import pandas as pd

# 读取数据集
titanic = pd.read_csv("data/titanic.csv")

# 显示数据集的前五行
titanic.head()
```
