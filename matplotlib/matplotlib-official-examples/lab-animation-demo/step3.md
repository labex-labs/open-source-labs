# Create the animation

We will use a for loop to iterate through each frame of the animation. In each iteration, we will clear the axis, plot the current frame, set the title, and pause for a short amount of time to allow the animation to be displayed.

```python
fig, ax = plt.subplots()

for i, img in enumerate(data):
    ax.clear()
    ax.imshow(img)
    ax.set_title(f"frame {i}")
    plt.pause(0.1)
```
