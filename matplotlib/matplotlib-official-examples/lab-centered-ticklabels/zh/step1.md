# 加载财务数据

首先，我们需要使用 Matplotlib 的 `cbook.get_sample_data()` 函数加载一些谷歌股价的财务数据。我们将使用最近 250 天的数据。

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Load some financial data; Google's stock price
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[-250:]  # get the last 250 days
```
