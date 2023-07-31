# Create Symlog Plot on both x-axis and y-axis

In the third subplot, we will create a `symlog` plot on both the x-axis and y-axis. We will also set the `linthresh` parameter to 0.015.

```python
ax2.plot(x, y3)
ax2.set_xscale('symlog')
ax2.set_yscale('symlog', linthresh=0.015)
ax2.grid()
ax2.set_ylabel('symlog both')
```
