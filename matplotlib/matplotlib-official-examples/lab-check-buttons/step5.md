# Define Callback Function

We need to define a callback function for the check buttons. This function will be called every time a check button is clicked. We will use this function to toggle the visibility of the corresponding line on the plot.

```python
def callback(label):
    ln = lines_by_label[label]
    ln.set_visible(not ln.get_visible())
    ln.figure.canvas.draw_idle()

check.on_clicked(callback)
```
