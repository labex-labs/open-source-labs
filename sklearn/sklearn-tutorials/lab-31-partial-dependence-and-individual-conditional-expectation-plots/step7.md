# Compute individual conditional expectation values for a specific feature

```python
x_index = 0
ice, axes = partial_dependence(model, X, features=[x_index], kind='individual')

# Plot the individual conditional expectation values
for i in range(len(ice)):
    plt.plot(axes[x_index], ice[i], color='lightgray')
plt.plot(axes[x_index], np.mean(ice, axis=0), color='blue')
plt.xlabel(feature_names[x_index])
plt.ylabel("Individual Conditional Expectation")
plt.title("Individual Conditional Expectation Plot")

plt.show()
```
