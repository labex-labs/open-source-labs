# Set the x-limits Using Scalars or Units

In this step, we will set the x-limits using scalars or units. We will use the `set_xlim` method to set the x-limits. We will set the x-limits to 2 and 6 using scalars in the current units for the bar graph in the second row and first column. We will set the x-limits to 2 cm and 6 cm using units for the bar graph in the second row and second column.

```python
axs[1, 0].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(2, 6)

axs[1, 1].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(2 * cm, 6 * cm)
```
