# 导入库并加载数据

首先，让我们导入所需的库并加载数据集。

```python
import pandas as pd

# 加载泰坦尼克号数据集
titanic = pd.read_csv("data/titanic.csv")

# 加载空气质量数据集
air_quality = pd.read_csv("data/air_quality_long.csv", index_col="date.utc", parse_dates=True)
```
