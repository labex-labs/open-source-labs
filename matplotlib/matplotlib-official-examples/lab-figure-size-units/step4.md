# Figure Size in Pixel

We can also specify the figure size in pixels. To do this, we need to convert the pixel value to inches. We can get the conversion factor from pixels to inches by dividing 1 by the dpi (dots per inch) value. We can then use this value as the figsize parameter in the subplots function. The code below shows how to create a figure with a size of 600 pixels x 200 pixels.

```python
px = 1/plt.rcParams['figure.dpi']  # pixel in inches
plt.subplots(figsize=(600*px, 200*px))
plt.show()
```
