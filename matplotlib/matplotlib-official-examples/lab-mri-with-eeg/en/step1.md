# Load MRI Data and Display the Image

The first step is to load the MRI data and display the image. We will use the `imshow()` function to display the image and `axis('off')` to remove the axis labels.

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("MRI_with_EEG")

# Load the MRI data (256x256 16-bit integers)
im = np.load('mri_data.npy')

# Plot the MRI image
ax0 = fig.add_subplot(2, 2, 1)
ax0.imshow(im, cmap='gray')
ax0.axis('off')
```
