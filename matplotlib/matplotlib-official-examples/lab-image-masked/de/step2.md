# Daten erstellen

Als nächstes werden wir einige Daten erstellen, die wir in unseren Plots verwenden. Für diesen Tutorial werden wir einen einfachen Liniendiagramm erstellen.

```python
# Create the data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y)
plt.show()
```
