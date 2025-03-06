# 准备环境并创建数据

在第一步中，我们将通过导入必要的库并创建用于可视化的示例数据来设置工作环境。我们将重点生成包含一些离群值的数据，以此展示使用断轴图（broken axis plot）的价值。

## 导入所需库

让我们从导入本教程所需的库开始。我们将使用 Matplotlib 进行可视化，使用 NumPy 生成和处理数值数据。

在 Jupyter Notebook 中创建一个新的单元格，并输入以下代码：

```python
import matplotlib.pyplot as plt
import numpy as np

print(f"NumPy version: {np.__version__}")
```

运行此单元格时，你应该会看到类似以下的输出：

```
NumPy version: 2.0.0
```

![numpy-version](../assets/screenshot-20250306-Um0MaTKw@2x.png)

确切的版本号可能会因你的环境而异，但这确认了库已正确安装并可以使用。

## 生成包含离群值的示例数据

现在，让我们创建一个包含一些离群值的示例数据集。我们将生成随机数，然后故意在某些位置添加较大的值来创建离群值。

创建一个新的单元格并添加以下代码：

```python
# Set random seed for reproducibility
np.random.seed(19680801)

# Generate 30 random points with values between 0 and 0.2
pts = np.random.rand(30) * 0.2

# Add 0.8 to two specific points to create outliers
pts[[3, 14]] += 0.8

# Display the first few data points to understand our dataset
print("First 10 data points:")
print(pts[:10])
print("\nData points containing outliers:")
print(pts[[3, 14]])
```

运行此单元格时，你应该会看到类似以下的输出：

```
First 10 data points:
[0.01182225 0.11765474 0.07404329 0.91088185 0.10502995 0.11190702
 0.14047499 0.01060192 0.15226977 0.06145634]

Data points containing outliers:
[0.91088185 0.97360754]
```

在这个输出中，你可以清楚地看到索引 3 和 14 处的值比其他值大得多。这些就是我们的离群值。我们的大多数数据点都低于 0.2，但这两个离群值高于 0.9，在我们的数据集中造成了显著的差异。

这种数据分布非常适合展示断轴图的实用性。在下一步中，我们将创建绘图结构并对其进行配置，以便正确显示主要数据和离群值。
