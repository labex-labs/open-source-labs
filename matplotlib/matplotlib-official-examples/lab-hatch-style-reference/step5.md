# Create the second set of hatching patterns

We will create the second set of hatching patterns by repeating each pattern twice to increase the density. We will use the following list:

```python
hatches = ['//', '\\\\', '||', '--', '++', 'xx', 'oo', 'OO', '..', '**']
```

We will use the same loop as before to create the rectangles.

```python
for ax, h in zip(axs.flat, hatches):
    hatches_plot(ax, h)
```
