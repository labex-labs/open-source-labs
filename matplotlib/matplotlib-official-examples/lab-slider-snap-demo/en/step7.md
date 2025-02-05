# Connect the Sliders to the Update Function

In this step, you will connect the sliders to the update function. This will ensure that the plot is updated whenever the slider values are changed.

```python
sfreq.on_changed(update)
samp.on_changed(update)
```
