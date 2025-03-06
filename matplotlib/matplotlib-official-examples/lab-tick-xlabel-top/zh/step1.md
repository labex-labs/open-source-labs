# 了解 Matplotlib 并创建 Notebook

在第一步中，你将了解 Matplotlib 并创建一个新的 Jupyter Notebook 来完成可视化任务。

## 什么是 Matplotlib？

Matplotlib 是一个用于在 Python 中创建静态、动态和交互式可视化图表的综合库。它提供了面向对象的 API，可将图表嵌入到应用程序中，被科学家、工程师和数据分析师广泛用于数据可视化。

## 创建新的 Notebook

在 Notebook 的第一个单元格中，让我们导入 Matplotlib 库。输入以下代码，然后按 Shift + Enter 运行该单元格：

```python
import matplotlib.pyplot as plt
import numpy as np

# Check the Matplotlib version
print(f"NumPy version: {np.__version__}")
```

![libraries-imported](../assets/screenshot-20250306-K6iIFfj1@2x.png)

运行此代码时，你应该会看到类似以下的输出：

```
NumPy version: 2.0.0
```

确切的版本号可能会因你的环境而异。

现在，你已经成功导入了 Matplotlib 并可以使用它了。`plt` 是 pyplot 模块的常用别名，它提供了类似 MATLAB 的接口来创建图表。
