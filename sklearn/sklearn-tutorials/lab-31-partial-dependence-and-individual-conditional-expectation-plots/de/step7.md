# Berechnen von Individual Conditional Expectation-Werten für ein bestimmtes Feature

```python
x_index = 0
ice, axes = partial_dependence(model, X, features=[x_index], kind='individual')

# Zeichnen der Individual Conditional Expectation-Werte
for i in range(len(ice)):
    plt.plot(axes[x_index], ice[i], color='hellgrau')
plt.plot(axes[x_index], np.mean(ice, axis=0), color='blau')
plt.xlabel(feature_names[x_index])
plt.ylabel("Individual Conditional Expectation")
plt.title("Individual Conditional Expectation Plot")

plt.show()
```
