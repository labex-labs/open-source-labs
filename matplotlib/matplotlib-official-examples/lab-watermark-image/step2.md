# Load Image

Next, we need to load the image that we want to overlay on the plot. We can use the `get_sample_data` method from the `matplotlib.cbook` module to load a sample image. In this example, we will use the `logo2.png` image.

```python
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)
```
