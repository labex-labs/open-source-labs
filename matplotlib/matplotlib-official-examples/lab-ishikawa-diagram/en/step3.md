# Create the Fishbone Diagram

Now we will create the fishbone diagram. We will start by creating a figure and axis object.

```python
fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
```

Next, we will set the x and y limits for the axis and turn off the axis.

```python
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')
```
