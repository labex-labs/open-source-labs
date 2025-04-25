# 总结

本实验展示了如何重写基本方法，以便在 Python Matplotlib 中一个艺术家（artist）可以包含另一个艺术家。我们创建了一个名为 `MyLine` 的自定义类，它继承自 `lines.Line2D`，并包含一个用于标注它的 `mtext.Text` 实例。然后我们将该线条添加到一个轴对象中并显示该绘图。
