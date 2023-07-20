# Create the Update Function

In this step, you will create the update function for the sliders. This function will update the plot when the slider values are changed.

```python
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()
```
