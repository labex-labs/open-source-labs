# Create the Plot

Now, we will create the plot using Matplotlib's `subplots` function. We will create two subplots, one for vertical lines and one for horizontal lines. We will set the figure size to (12, 6) for better visibility.

```python
# Create the plot
fig, (vax, hax) = plt.subplots(1, 2, figsize=(12, 6))
```
