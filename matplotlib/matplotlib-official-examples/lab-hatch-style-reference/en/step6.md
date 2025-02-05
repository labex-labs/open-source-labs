# Create the third set of hatching patterns

We will create the third set of hatching patterns by combining two patterns to create a new one. We will use the following list:

```python
hatches = ['/o', '\\|', '|*', '-\\', '+o', 'x*', 'o-', 'O|', 'O.', '*-']
```

We will use the same loop as before to create the rectangles.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
