# Set the major and minor locators

```python
# Set the major locator
ax.xaxis.set_major_locator(MultipleLocator(20))
# Set the major formatter
ax.xaxis.set_major_formatter('{x:.0f}')
# Set the minor locator
ax.xaxis.set_minor_locator(MultipleLocator(5))
```

Here, we set the major locator to place ticks at multiples of 20, set the major formatter to label the major ticks with ".0f" formatting, and set the minor locator to place ticks at multiples of 5.
