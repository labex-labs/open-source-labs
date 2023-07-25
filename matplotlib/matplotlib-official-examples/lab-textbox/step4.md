# Create the Textbox Widget

We create the Textbox widget and add it to the figure. The `on_submit` method is used to trigger the `submit` function when the user presses enter in the textbox or leaves the textbox. We also set the initial value of the Textbox widget to `t ** 2`.

```python
axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate", textalignment="center")
text_box.on_submit(submit)
text_box.set_val("t ** 2")  # Trigger `submit` with the initial string.
```
