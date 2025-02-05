# Create the Animation Frames

We will now create the frames for the animation. We will be using a for loop to generate 60 frames. In each iteration of the loop, we will be updating the x and y data and then creating a new image object using the imshow method. We will then append the image object to the ims list.

```python
ims = []
for i in range(60):
    x += np.pi / 15
    y += np.pi / 30
    im = ax.imshow(f(x, y), animated=True)
    if i == 0:
        ax.imshow(f(x, y))  # show an initial one first
    ims.append([im])
```
