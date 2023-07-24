# Set tick labels for the second y-axis

We can set the tick labels for the second y-axis using the `set_xticks` function and passing in the tick locations and labels as arguments.

```python
ax2.set_xticks([0., .5*np.pi, np.pi, 1.5*np.pi, 2*np.pi],
               labels=["$0$", r"$\frac{1}{2}\pi$",
                       r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
```
