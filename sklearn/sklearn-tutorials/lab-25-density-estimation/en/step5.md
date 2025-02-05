# Visualize the density estimate

Finally, we can visualize the density estimate using a histogram and the estimated density function. We can plot the histogram of the original data as well as the estimated density function.

```python
import matplotlib.pyplot as plt

bins = np.linspace(-5, 5, 50)
plt.hist(X, bins=bins, density=True, alpha=0.5, label='Histogram')
plt.plot(X, np.exp(scores), color='red', label='Kernel Density Estimate')
plt.legend()
plt.show()
```
