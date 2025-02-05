# 导入 Pandas 并加载数据

首先，我们将导入 pandas 库，并从 CSV 文件中加载空气质量数据。

```python
# 导入 pandas 库
import pandas as pd

# 加载空气质量数据
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
```
