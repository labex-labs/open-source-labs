# Python Matplotlib MRI Image Visualization Lab

## Introduction

In this lab, you will learn how to read an MRI image into a NumPy array and display it in grayscale using `matplotlib` library.

## Steps

### Step 1: Import required libraries

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook
```

### Step 2: Load the MRI image data

We will use the `get_sample_data` function from `matplotlib` to load the sample MRI image. The image is in 256x256 16-bit integer format.

```python
with cbook.get_sample_data('s1045.ima.gz') as dfile:
    im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))
```

### Step 3: Display the MRI image

We will use `imshow` function from `matplotlib` to display the MRI image in grayscale.

```python
fig, ax = plt.subplots(num="MRI_demo")
ax.imshow(im, cmap="gray")
ax.axis('off')
plt.show()
```

## Summary

In this lab, you learned how to load an MRI image into a NumPy array and display it in grayscale using `matplotlib` library. You can use this knowledge to visualize other medical images as well.
