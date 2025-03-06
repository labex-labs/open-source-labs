# 加载并查看图像

既然我们已经导入了所需的库，接下来就需要加载想要叠加到绘图上的图像。Matplotlib 提供了一些示例图像供我们练习使用。

1. 在你的 Notebook 中创建一个新单元格，并输入以下代码：

```python
# Load the sample image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Display information about the image
print(f"Image shape: {im.shape}")
print(f"Image data type: {im.dtype}")

# Display the image
plt.figure(figsize=(4, 4))
plt.imshow(im)
plt.axis('off')  # Hide axis
plt.title('Matplotlib Logo')
plt.show()
```

这段代码的功能如下：

- 使用 `cbook.get_sample_data()` 从 Matplotlib 的示例数据集中加载名为 'logo2.png' 的示例图像。
- 使用 `image.imread()` 将图像文件读取为 NumPy 数组。
- 打印图像的尺寸和数据类型信息。
- 创建一个图形，并使用 `plt.imshow()` 显示图像。
- 使用 `plt.axis('off')` 隐藏坐标轴刻度和标签。
- 为图形添加标题。
- 使用 `plt.show()` 显示图形。

2. 按下 Shift + Enter 运行该单元格。

输出结果应显示图像的相关信息，并展示 Matplotlib 的徽标。图像的形状表示图像的尺寸（高度、宽度、颜色通道），数据类型则告诉我们图像数据的存储方式。

![image-info](../assets/screenshot-20250306-cqkw4mpg@2x.png)

这一步非常重要，因为它有助于我们了解将用作叠加层的图像。我们可以看到它的外观和尺寸，这在决定如何将其放置在绘图上时会很有用。
