# 创建 Jupyter Notebook 并导入所需库

在 Notebook 的第一个单元格中，输入以下代码以导入必要的库：

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
```

让我们来了解一下这些库的作用：

- `matplotlib.pyplot`（别名为 `plt`）：一组使 Matplotlib 像 MATLAB 一样工作的函数，为创建绘图提供了便捷的接口。
- `numpy`（别名为 `np`）：Python 中用于科学计算的基础包，我们将用它来进行数据处理。
- `matplotlib.cbook`：Matplotlib 的实用函数集合，包括获取示例数据的函数。
- `matplotlib.image`：Matplotlib 中与图像相关功能的模块，我们将用它来读取和显示图像。

点击 Notebook 顶部的“运行”按钮或按 Shift + Enter 来运行该单元格。

![libraries-imported](../assets/screenshot-20250306-18gJ6FRZ@2x.png)

此单元格执行完成后应无任何输出，这表明所有库都已成功导入。
