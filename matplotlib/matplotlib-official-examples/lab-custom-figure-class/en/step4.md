# Plot the data using custom figure subclass

Use the `plt.figure()` function to plot the data using the custom figure subclass `WatermarkFigure`. In this example, we will add the watermark text "draft" to the plot.

```python
plt.figure(FigureClass=WatermarkFigure, watermark='draft')
plt.plot(x, y)
```
