# Create a Figure and Axes

We will create a figure and an axes object using `plt.subplots()`. The `imshow()` function is used to display the random data as an image.

```python
fig, ax = plt.subplots()

image = np.random.uniform(size=(10, 10))
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('dropped spines')
```
