# Création d'un graphique en barres

Un autre type de graphique courant est le graphique en barres. Les graphiques en barres sont utiles pour comparer les valeurs de différentes catégories.

```python
# Create the data
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 1, 9, 4]

# Create the bar chart
plt.bar(x, y)

# Add title and axis labels
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()
```
