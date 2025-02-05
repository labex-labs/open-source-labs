# Display the MRI image

We will use `imshow` function from `matplotlib` to display the MRI image in grayscale.

```python
fig, ax = plt.subplots(num="MRI_demo")
ax.imshow(im, cmap="gray")
ax.axis('off')
plt.show()
```
