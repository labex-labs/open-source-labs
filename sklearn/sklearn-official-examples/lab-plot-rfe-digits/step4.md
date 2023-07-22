# Visualize the Feature Rankings

Finally, we will plot the feature rankings using the Matplotlib library. We will use the `matshow()` function to display the rankings as an image. We will also add a color bar and a title to the plot.

```python
import matplotlib.pyplot as plt

plt.matshow(ranking, cmap=plt.cm.Blues)
plt.colorbar()
plt.title("Ranking of pixels with RFE")
plt.show()
```
