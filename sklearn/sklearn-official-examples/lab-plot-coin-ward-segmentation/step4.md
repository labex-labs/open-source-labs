# Plot the Results

Finally, we can plot the results on an image. We will use matplotlib to plot the rescaled image and the contours of the clusters. We will loop through each cluster and plot the contour of the pixels in that cluster.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(5, 5))
plt.imshow(rescaled_coins, cmap=plt.cm.gray)
for l in range(n_clusters):
    plt.contour(
        label == l,
        colors=[
            plt.cm.nipy_spectral(l / float(n_clusters)),
        ],
    )
plt.axis("off")
plt.show()
```
