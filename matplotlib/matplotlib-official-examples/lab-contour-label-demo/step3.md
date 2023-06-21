# Label contours with arbitrary strings using a dictionary

We can also label contours with arbitrary strings using a dictionary. This will allow us to label the contours with custom labels. In this example, we will use a list of strings to label the contours.

```python
fig1, ax1 = plt.subplots()
CS1 = ax1.contour(X, Y, Z)

fmt = {}
strs = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
for l, s in zip(CS1.levels, strs):
    fmt[l] = s

ax1.clabel(CS1, CS1.levels[::2], inline=True, fmt=fmt, fontsize=10)
```
