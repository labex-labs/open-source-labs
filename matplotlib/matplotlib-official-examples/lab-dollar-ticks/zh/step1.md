# 安装库并创建示例数据

在第一步中，我们将导入必要的库，并为绘图创建示例金融数据。我们需要导入用于可视化的 Matplotlib 和用于数据生成的 NumPy。

在你的 Notebook 的第一个单元格中，输入并运行以下代码以导入所需的库：

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Display plots inline in the notebook
%matplotlib inline

print("Libraries imported successfully!")
```

运行代码后（按 Shift + Enter），你应该会看到输出：

```
Libraries imported successfully!
```

![libraries-imported](../assets/screenshot-20250306-BN9E08ez@2x.png)

现在，让我们创建一些用于可视化的示例金融数据。金融数据通常表示随时间变化的值，因此我们将创建一个简单的数据集，它可能代表一段时间内的每日收入。

在一个新的单元格中，添加并运行以下代码：

```python
# Set a random seed for reproducibility
np.random.seed(42)

# Generate financial data: 30 days of revenue data
days = np.arange(1, 31)
daily_revenue = np.random.uniform(low=1000, high=5000, size=30)

print("Sample of daily revenue data (first 5 days):")
for i in range(5):
    print(f"Day {days[i]}: ${daily_revenue[i]:.2f}")
```

运行此代码后，你将看到示例收入数据的前 5 天：

```
Sample of daily revenue data (first 5 days):
Day 1: $3745.40
Day 2: $3992.60
Day 3: $2827.45
Day 4: $4137.54
Day 5: $1579.63
```

这个示例数据代表了 30 天内每日收入在 1000 美元到 5000 美元之间的值。我们将在下一步中使用这些数据来创建我们的绘图。
