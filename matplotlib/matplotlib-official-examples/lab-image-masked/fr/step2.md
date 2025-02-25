# Création de données

Ensuite, nous allons créer des données à utiliser dans nos graphiques. Pour ce tutoriel, nous allons créer un graphique en ligne simple.

```python
# Create the data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y)
plt.show()
```
