# Online Learning of a Dictionary of Parts of Faces

## Introduction

This lab demonstrates how to use the scikit-learn API to process a large dataset of faces and learn a set of 20 x 20 image patches that represent faces. The key aspect of this lab is the use of online learning, where we load and process images one at a time and extract 50 random patches from each image. We accumulate 500 patches (from 10 images) and then run the online KMeans object, MiniBatchKMeans' partial_fit method.

## Steps

### Step 1: Load the Data

We first load the Olivetti faces dataset from scikit-learn.

```python
from sklearn import datasets

faces = datasets.fetch_olivetti_faces()
```

### Step 2: Learn the Dictionary of Images

We use MiniBatchKMeans to learn the dictionary of images. We set the number of clusters to 81, set a random state, and enable verbose mode. We then create a buffer to store patches and iterate through each image in the dataset. We extract 50 patches from each image and reshape the data. We then append the data to the buffer and increment the index. If the index is a multiple of 10, we concatenate the buffer and run partial_fit on the data. If the index is a multiple of 100, we print a message indicating the number of patches that have been fitted so far.

```python
import time
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.image import extract_patches_2d

print("Learning the dictionary... ")
rng = np.random.RandomState(0)
kmeans = MiniBatchKMeans(n_clusters=81, random_state=rng, verbose=True, n_init=3)
patch_size = (20, 20)

buffer = []
t0 = time.time()

# The online learning part: cycle over the whole dataset 6 times
index = 0
for _ in range(6):
    for img in faces.images:
        data = extract_patches_2d(img, patch_size, max_patches=50, random_state=rng)
        data = np.reshape(data, (len(data), -1))
        buffer.append(data)
        index += 1
        if index % 10 == 0:
            data = np.concatenate(buffer, axis=0)
            data -= np.mean(data, axis=0)
            data /= np.std(data, axis=0)
            kmeans.partial_fit(data)
            buffer = []
        if index % 100 == 0:
            print("Partial fit of %4i out of %i" % (index, 6 * len(faces.images)))

dt = time.time() - t0
print("done in %.2fs." % dt)
```

### Step 3: Plot the Results

Finally, we plot the patches of faces and display the training time.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(4.2, 4))
for i, patch in enumerate(kmeans.cluster_centers_):
    plt.subplot(9, 9, i + 1)
    plt.imshow(patch.reshape(patch_size), cmap=plt.cm.gray, interpolation="nearest")
    plt.xticks(())
    plt.yticks(())


plt.suptitle(
    "Patches of faces\nTrain time %.1fs on %d patches" % (dt, 8 * len(faces.images)),
    fontsize=16,
)
plt.subplots_adjust(0.08, 0.02, 0.92, 0.85, 0.08, 0.23)

plt.show()
```

## Summary

In this lab, we demonstrated how to use online learning to process a large dataset of faces and learn a set of image patches that represent faces. We used MiniBatchKMeans to learn the dictionary of images and plotted the results.
