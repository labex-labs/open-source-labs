# Save the Numpy Array to a Pillow Image

Now that we have the numpy array, we can pass it off to Pillow and save it in any format supported by Pillow. In this example, we will save the plot as a BMP image.

```python
from PIL import Image

im = Image.fromarray(rgba)
im.save("test.bmp")
```
