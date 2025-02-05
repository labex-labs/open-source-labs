# Create the plot

Now, we create a plot with two y-axes using the `subplots()` function of `matplotlib.pyplot`. We also connect the `ylim_changed` event of the first axis to the `convert_ax_c_to_celsius()` function.

```python
fig, ax_f = plt.subplots()
ax_c = ax_f.twinx()

ax_f.callbacks.connect("ylim_changed", convert_ax_c_to_celsius)
```
