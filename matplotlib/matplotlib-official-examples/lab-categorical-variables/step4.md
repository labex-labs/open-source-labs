# Scatter Plot

We can also create a scatter plot to show the relationship between two categorical variables. In this case, we will use the same fruit data and add some random noise to the counts to create a second variable.

```python
noise = np.random.rand(len(values)) * 5
plt.scatter(names, values + noise)
plt.title('Fruit Counts with Noise')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.show()
```
