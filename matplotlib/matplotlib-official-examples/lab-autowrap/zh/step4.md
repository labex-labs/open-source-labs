# 控制文本位置和样式

我们还可以控制 Matplotlib 绘图中文字的位置和样式。尝试在你的脚本中添加以下代码：

```python
plt.text(2, 8, "Top Left", fontsize=12, color='red')
plt.text(8, 8, "Top Right", fontsize=12, color='blue')
plt.text(2, 2, "Bottom Left", fontsize=12, color='green')
plt.text(8, 2, "Bottom Right", fontsize=12, color='purple')
```

这将在我们的绘图中添加四个文本元素，每个元素都有不同的颜色、字体大小和位置。
