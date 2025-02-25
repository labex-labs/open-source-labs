# Création d'un graphique en nuage de points

En plus des graphiques en ligne, Matplotlib nous permet également de créer des graphiques en nuage de points. Les graphiques en nuage de points sont utiles pour visualiser la relation entre deux variables.

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
