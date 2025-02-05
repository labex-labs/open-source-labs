# Create Symlog Plot on x-axis

In the first subplot, we will create a `symlog` plot on the x-axis. We will also add a minor grid to the x-axis.

```python
ax0.plot(x, y1)
ax0.set_xscale('symlog')
ax0.set_ylabel('symlogx')
ax0.grid()
ax0.xaxis.grid(which='minor')
```
