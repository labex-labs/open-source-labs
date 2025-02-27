# Erstellen und Visualisieren von Individual Conditional Expectation Plots

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, kind='individual')

# Setzen der Figurgröße und des Titels
fig.set_size_inches(10, 8)
fig.suptitle('Individual Conditional Expectation Plots')

plt.show()
```
