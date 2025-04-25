# 总结

在本实验中，我们学习了如何在 Matplotlib 中创建多色线条。我们使用 `LineCollection` 函数创建一组线段，并根据它们的导数分别为其着色。我们还学习了如何使用边界规范为线段着色。我们使用 `Normalize` 函数将 `dydx` 值在其最小值和最大值之间进行归一化，并使用 `ListedColormap` 函数创建一个包含三种颜色（红色、绿色和蓝色）的颜色映射。我们使用 `BoundaryNorm` 函数创建一个边界为 -1、-0.5、0.5 和 1 的边界规范，以及上述 `ListedColormap`。最后，我们使用 `subplots` 函数创建一个 2x1 的子图网格，并使用 `sharex` 和 `sharey` 参数在子图之间共享 x 轴和 y 轴。然后，我们使用 `show` 函数显示绘图。
