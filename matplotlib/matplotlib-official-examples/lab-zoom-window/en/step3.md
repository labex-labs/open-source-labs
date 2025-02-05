# Connect the event to the function

Now, we connect the button press event in the first window to the on_press function we just defined.

```python
figsrc.canvas.mpl_connect('button_press_event', on_press)
```
