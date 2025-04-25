# 创建第一个文本对象

第一步是使用 `~.Axes.text` 创建第一个文本对象。这个文本对象将是连接过程的起点。以下代码在绘图上的位置 (0.1, 0.5) 创建了一个红色文本对象，内容为“Matplotlib”。

```python
text = ax.text(.1,.5, "Matplotlib", color="red")
```
