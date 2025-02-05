# 导入必要的库并加载数据

首先，我们需要导入所需的 Python 库并加载空气质量数据。数据将被读入一个 pandas DataFrame，它是一种二维带标签的数据结构。

```python
# 导入必要的库
import pandas as pd
import matplotlib.pyplot as plt

# 加载空气质量数据
air_quality = pd.read_csv("data/air_quality_no2_long.csv")

# 将 "date.utc" 列重命名为 "datetime"
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
```
