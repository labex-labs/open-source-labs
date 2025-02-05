# Create the RangeSlider

We will now create the RangeSlider widget, which will allow us to adjust the threshold of the image. We will create a new axis for the slider and add it to the figure.

```python
slider_ax = fig.add_axes([0.20, 0.1, 0.60, 0.03])
slider = RangeSlider(slider_ax, "Threshold", img.min(), img.max())
```
