# 总结

在本实验中，我们学习了如何使用 `multiprocessing` 库和 Matplotlib 来绘制从单独进程生成的数据。我们创建了两个类——`ProcessPlotter` 和 `NBPlot`——分别用于处理绘图和数据生成。`NBPlot` 类生成随机数据，并通过管道将其发送到 `ProcessPlotter` 类，然后 `ProcessPlotter` 类实时绘制这些数据。
