# Create Subplots

Next, we create the subplots using `plt.subplot_mosaic`. We will create a 3x2 grid of subplots and label them as follows:

- The top-left plot will be labeled as "a)"
- The bottom-left plot will be labeled as "b)"
- The top-right and bottom-right plots will be labeled as "c)" and "d)" respectively.

```python
fig, axs = plt.subplot_mosaic([['a)', 'c)'], ['b)', 'c)'], ['d)', 'd)']], layout='constrained')
```
