# Create the first set of hatching patterns

We will create the first set of hatching patterns using the following list:

```python
hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
```

We will then use a loop to create a rectangle with each hatching pattern and add it to a subplot.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
