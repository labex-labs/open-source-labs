# Add a Slider

We add a horizontal slider to the GUI that allows the user to adjust the frequency of the sine wave. We also define a function that updates the plot according to the value of the slider.

```python
def update_frequency(new_val):
    # retrieve frequency
    f = float(new_val)

    # update data
    y = 2 * np.sin(2 * np.pi * f * t)
    line.set_data(t, y)

    # required to update canvas and attached toolbar!
    canvas.draw()

slider_update = tkinter.Scale(root, from_=1, to=5, orient=tkinter.HORIZONTAL,
                              command=update_frequency, label="Frequency [Hz]")
```
