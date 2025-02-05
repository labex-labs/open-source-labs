# Create the Update Function

We will now create the function that will update the sine wave every time we adjust the sliders. The function will take in the values of the amplitude and frequency sliders, and update the sine wave accordingly.

```python
def update(val):
    line.set_ydata(f(t, amp_slider.val, freq_slider.val))
    fig.canvas.draw_idle()
```
