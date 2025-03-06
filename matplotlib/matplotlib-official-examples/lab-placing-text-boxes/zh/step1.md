# 创建 Jupyter Notebook 并准备数据

在第一步中，我们将创建一个新的 Jupyter Notebook 并为可视化准备数据。

## 创建新的 Notebook

在 Notebook 的第一个单元格中，让我们导入必要的库。输入以下代码，然后点击“运行”按钮或按下 Shift + Enter 来运行它：

```python
import matplotlib.pyplot as plt
import numpy as np
```

![libraries-imported](../assets/screenshot-20250306-Azb1cb3S@2x.png)

这段代码导入了两个重要的库：

- `matplotlib.pyplot`：一组让 matplotlib 像 MATLAB 一样工作的函数集合
- `numpy`：Python 中用于科学计算的基础包

## 创建示例数据

现在，让我们创建一些用于可视化的示例数据。在一个新的单元格中，输入并运行以下代码：

```python
# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate 10,000 random numbers from a normal distribution
x = 30 * np.random.randn(10000)

# Calculate basic statistics
mu = x.mean()
median = np.median(x)
sigma = x.std()

# Display the statistics
print(f"Mean (μ): {mu:.2f}")
print(f"Median: {median:.2f}")
print(f"Standard Deviation (σ): {sigma:.2f}")
```

当你运行这个单元格时，你应该会看到类似于以下的输出：

```
Mean (μ): -0.31
Median: -0.28
Standard Deviation (σ): 29.86
```

具体的值可能会略有不同。我们创建了一个包含 10000 个从正态分布中生成的随机数的数据集，并计算了三个重要的统计量：

1. 均值 (μ)：所有数据点的平均值
2. 中位数：数据按顺序排列后的中间值
3. 标准差 (σ)：衡量数据分散程度的指标

这些统计量将在后面用于为我们的可视化添加注释。
