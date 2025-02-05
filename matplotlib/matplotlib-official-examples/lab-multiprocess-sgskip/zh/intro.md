# 简介

在本实验中，你将学习如何使用多进程库和Matplotlib来绘制从单独进程生成的数据。我们将创建两个类——`ProcessPlotter` 和 `NBPlot`——分别用于处理绘图和数据生成。`NBPlot` 类将生成随机数据，并通过管道将其发送到 `ProcessPlotter` 类，然后该类将实时绘制数据。

## 虚拟机使用提示

虚拟机启动完成后，点击左上角切换到**笔记本**标签页，以访问Jupyter Notebook进行练习。

有时，你可能需要等待几秒钟让Jupyter Notebook完成加载。由于Jupyter Notebook的限制，操作验证无法自动化。

如果你在学习过程中遇到问题，随时向Labby提问。课程结束后提供反馈，我们将立即为你解决问题。
