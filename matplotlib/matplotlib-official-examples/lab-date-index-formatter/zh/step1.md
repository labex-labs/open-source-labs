# 导入所需的库和数据

我们首先需要导入所需的库，即 `matplotlib`、`numpy` 和 `matplotlib.cbook`。我们还需要从 `mpl-data/sample_data` 目录中加载一个来自雅虎 CSV 数据的 numpy 记录数组，其字段包括日期、开盘价、最高价、最低价、收盘价、成交量、调整收盘价。记录数组在日期列中将日期存储为具有日单位（'D'）的 `np.datetime64`。我们将使用这些数据来绘制金融时间序列图。

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# 从 sample_data 目录加载数据
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[:9]  # 获取前 9 天的数据
```
