# Importing Image Data

To begin, we need to import the necessary libraries and load the image data into a NumPy array. In our case, we will use the `PIL` library to load the image, and then convert it into a NumPy array.

```python
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open('./stinkbug.png'))
```
