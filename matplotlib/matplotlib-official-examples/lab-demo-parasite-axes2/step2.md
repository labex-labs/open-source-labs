# Create Host and Parasite Axes

We will create a host axis and two parasite axes using the `host_subplot()` and `twinx()` functions. The `host_subplot()` function creates a host axis, and the `twinx()` function creates parasite axes that share the same x-axis with the host axis.

```python
host = host_subplot(111, axes_class=axisartist.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()
```
