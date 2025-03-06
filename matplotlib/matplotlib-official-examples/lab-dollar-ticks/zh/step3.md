# 用美元符号格式化 y 轴标签

现在我们已经有了基本的绘图，接下来让我们对 y 轴标签进行格式化，使其显示美元符号。这将使我们的金融数据更易读，呈现效果也更专业。

为了格式化 y 轴上的刻度标签，我们将使用 Matplotlib 的 `ticker` 模块，该模块提供了各种格式化选项。具体来说，我们将使用 `StrMethodFormatter` 类为 y 轴创建一个自定义格式化器。

在你的 Notebook 的新单元格中，添加并运行以下代码：

```python
# Import the necessary module for formatting
import matplotlib.ticker as ticker

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)

# Format y-axis with dollar signs
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)

# Add labels and title
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Revenue ($)', fontsize=12)
ax.set_title('Daily Revenue Over 30 Days', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()

print("Plot with dollar-formatted y-axis created!")
```

运行此代码后，你应该会看到一个新的绘图，其 y 轴标签带有美元符号。

让我们解释一下这段代码的关键部分：

```python
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)
```

这个格式化字符串的作用如下：

- `$` — 在每个标签的开头添加一个美元符号
- `{x:,.2f}` — 对数字进行如下格式化：
  - `,` — 使用逗号作为千位分隔符（例如，1,000 而不是 1000）
  - `.2f` — 保留两位小数（例如，$1,234.56）

这个格式化器适用于 y 轴上的所有主要刻度标签。注意，现在绘图清晰地表明这些值是以美元为单位的，这使得它更适合用于金融数据可视化。
