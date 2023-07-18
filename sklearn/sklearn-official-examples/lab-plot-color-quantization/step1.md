# Load and Display the Original Image

We will begin by loading and displaying the original image of the Summer Palace.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_sample_image

# Load the Summer Palace photo
china = load_sample_image("china.jpg")

# Display the original image
plt.figure()
plt.axis("off")
plt.title("Original Image")
plt.imshow(china)
plt.show()
```
