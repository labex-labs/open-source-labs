# 简介

本教程演示如何使用 Matplotlib 生成高分辨率的三角剖分等值线图。三角剖分等值线是一种用于在非结构化三角形网格上表示数据的技术。当数据是在不规则间隔的点上收集时，或者当数据本质上是三角形时，经常会用到它。本教程将展示如何生成一组随机点，对这些点进行 Delaunay 三角剖分，屏蔽网格中的一些三角形，细化和插值数据，最后使用 Matplotlib 的 `tricontour` 函数绘制细化后的数据。

## 虚拟机使用提示

虚拟机启动完成后，点击左上角切换到 **笔记本** 标签页，以访问 Jupyter Notebook 进行练习。

有时，你可能需要等待几秒钟让 Jupyter Notebook 完成加载。由于 Jupyter Notebook 的限制，操作的验证无法自动化。

如果你在学习过程中遇到问题，随时向 Labby 提问。课程结束后提供反馈，我们会及时为你解决问题。
