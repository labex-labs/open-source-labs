# Summary

In this lab, we learned how to use the `multiprocessing` library and Matplotlib to plot data generated from a separate process. We created two classes - `ProcessPlotter` and `NBPlot` - to handle the plotting and data generation, respectively. The `NBPlot` class generated random data and sent it to the `ProcessPlotter` class through a pipe, which then plotted the data in real-time.
