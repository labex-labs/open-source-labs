# 显示绘图

一旦你创建并自定义了所有文本对象，就可以使用 `plt.show()` 显示绘图。以下代码块展示了该绘图的完整代码。

```python
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 20
ax = plt.figure().add_subplot(xticks=[], yticks=[])

# 第一个单词，使用 text() 创建。
text = ax.text(.1,.5, "Matplotlib", color="red")
# 后续单词，使用 annotate() 定位，相对于前一个单词。
text = ax.annotate(
    " says,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # 自定义属性
text = ax.annotate(
    " hello", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # 自定义属性
text = ax.annotate(
    " world!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # 自定义属性

plt.show()
```
