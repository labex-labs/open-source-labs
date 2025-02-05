# Visualizing the Dataset

To get a better understanding of the dataset, we can visualize a sample image using matplotlib. The following code displays the last digit in the dataset:

```python
import matplotlib.pyplot as plt

# Display the last digit
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
```
