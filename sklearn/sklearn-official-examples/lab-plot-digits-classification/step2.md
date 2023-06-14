# Load and Visualize the Digits Dataset

We will load the digits dataset which consists of 8x8 pixel images of digits. We will use `imshow()` method from `matplotlib` to visualize the first 4 images along with their corresponding labels.

```python
digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)
```


