# Register the Update Function with the Sliders

Next, we will register the update function with each slider so that the function is called every time we adjust the sliders.

```python
freq_slider.on_changed(update)
amp_slider.on_changed(update)
```
