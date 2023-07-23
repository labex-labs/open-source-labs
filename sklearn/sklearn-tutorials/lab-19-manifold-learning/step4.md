# Compare Results

Compare the results of the different manifold learning algorithms. Visualize the transformed data to see how the algorithms have preserved the underlying structure of the data.

```python
import matplotlib.pyplot as plt

# Create a scatter plot of the transformed data
plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y)
plt.title('Manifold Learning')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.show()
```
