# 总结

本实验展示了如何在 Matplotlib 中处理日期精度和纪元。我们可以使用`mdates.set_epoch`方法将纪元设置为旧的默认值或新的默认值。然后，我们可以使用`mdates.date2num`函数将`datetime`或`numpy.datetime64`对象转换为 Matplotlib 日期，并使用`mdates.num2date`函数对日期进行往返转换，以确保转换的准确性。我们还可以绘制具有不同纪元的数据，以观察绘图中的差异。
