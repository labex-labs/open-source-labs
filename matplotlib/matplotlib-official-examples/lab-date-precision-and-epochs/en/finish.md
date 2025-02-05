# Summary

This lab demonstrates how to handle date precision and epochs in Matplotlib. We can set the epoch to the old default or the new default using the `mdates.set_epoch` method. We can then convert `datetime` or `numpy.datetime64` objects to Matplotlib dates using the `mdates.date2num` function, and round-trip the dates using the `mdates.num2date` function to make sure the conversion is accurate. We can also plot data with different epochs to observe the differences in the plot.
