# 优化绘图以实现更好的金融数据可视化

既然我们已经完成了基本的货币格式设置，接下来让我们进一步优化绘图，使其更有助于金融数据分析。我们将进行以下几方面的改进：

1. 添加一条水平线，显示平均每日收入
2. 添加注释，突出显示收入最高和最低的日期
3. 自定义刻度参数，提高可读性
4. 使用更具描述性的标题和图例

在你的 Notebook 的新单元格中，添加并运行以下代码：

```python
# Import the necessary module for formatting
import matplotlib.ticker as ticker

# Create a figure and axes
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue',
        linewidth=2, markersize=6, label='Daily Revenue')

# Calculate statistics
avg_revenue = np.mean(daily_revenue)
max_revenue = np.max(daily_revenue)
min_revenue = np.min(daily_revenue)
max_day = days[np.argmax(daily_revenue)]
min_day = days[np.argmin(daily_revenue)]

# Add a horizontal line for average revenue
ax.axhline(y=avg_revenue, color='r', linestyle='--', alpha=0.7,
           label=f'Average Revenue: ${avg_revenue:.2f}')

# Format y-axis with dollar signs
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)

# Customize tick parameters
ax.tick_params(axis='both', which='major', labelsize=10)
ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
ax.xaxis.set_major_locator(ticker.MultipleLocator(base=5))

# Add annotations for max and min revenue
ax.annotate(f'Max: ${max_revenue:.2f}', xy=(max_day, max_revenue),
            xytext=(max_day+1, max_revenue+200),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

ax.annotate(f'Min: ${min_revenue:.2f}', xy=(min_day, min_revenue),
            xytext=(min_day+1, min_revenue-200),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

# Add labels and title
ax.set_xlabel('Day of Month', fontsize=12)
ax.set_ylabel('Revenue ($)', fontsize=12)
ax.set_title('Daily Revenue Analysis - 30 Day Period', fontsize=14, fontweight='bold')

# Set x-axis limits to show a bit of padding
ax.set_xlim(0, 31)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add legend
ax.legend(loc='upper right', fontsize=10)

# Display the plot
plt.tight_layout()
plt.show()

print("Enhanced financial plot created successfully!")
```

运行此代码后，你将看到一个信息更加丰富的绘图，具备以下特点：

1. y 轴采用美元符号格式化
2. 有一条红色虚线水平线，显示平均收入
3. 有注释指向收入最高和最低的日期
4. 刻度标记更清晰，间距更合理
5. 有一个图例，说明每个元素的含义

让我们解释一下其中一些新元素：

- `ax.axhline()` — 在指定的 y 值处添加一条水平线（在本例中为平均收入）
- `ax.yaxis.set_major_locator()` — 控制 y 轴上显示的刻度标记数量
- `ax.xaxis.set_major_locator()` — 设置 x 轴以 5 天为间隔显示刻度
- `ax.annotate()` — 添加带有箭头的文本注释，指向特定的数据点
- `ax.legend()` — 添加一个图例，解释绘图上的不同元素

这些改进通过突出关键统计数据并使数据更易于解读，让绘图在金融分析中更具实用性。
