# Display the Image

Now we can display the image using Matplotlib's `imshow` method. We will also turn off the axis so that we only see the image.

```python
fig, ax = plt.subplots()
im = ax.imshow(image)
ax.axis('off')
```
