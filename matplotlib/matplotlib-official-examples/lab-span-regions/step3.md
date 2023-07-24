# Create the Plot

Now we will create the plot using `matplotlib.pyplot`. We will plot the sine wave and add a horizontal line at y=0.

```python
fig, ax = plt.subplots()

ax.plot(t, s, color='black')
ax.axhline(0, color='black')
```
