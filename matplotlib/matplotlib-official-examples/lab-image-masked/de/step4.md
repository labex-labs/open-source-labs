# Erstellen eines Scatterplots

Neben Liniendiagrammen ermöglicht Matplotlib auch das Erstellen von Scatterplots. Scatterplots eignen sich zur Visualisierung der Beziehung zwischen zwei Variablen.

```python
# Create the data
x = np.random.rand(50)
y = np.random.rand(50)

# Create the scatter plot
plt.scatter(x, y)

# Add title and axis labels
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
```
