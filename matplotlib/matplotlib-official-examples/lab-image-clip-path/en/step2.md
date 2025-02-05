# Load the Image

We will use the `get_sample_data` method from `cbook` to load a sample image. This method returns a file-like object, which we can pass to `imshow` to display the image.

```python
with cbook.get_sample_data('grace_hopper.jpg') as image_file:
    image = plt.imread(image_file)
```
