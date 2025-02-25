# Personnalisez le diagramme en boîte

Nous pouvons personnaliser le diagramme en boîte en changeant l'apparence de la boîte, des barres d'agrégation et des valeurs aberrantes. Nous pouvons également créer plusieurs diagrammes en boîte sur la même figure pour comparer différents groupes de données. Voici quelques exemples de personnalisation du diagramme en boîte :

```python
# Créez un diagramme en boîte encadré
plt.boxplot(data, notch=True)
plt.show()

# Changez les symboles des points aberrants en diamants verts
plt.boxplot(data, flierprops=dict(marker='D', markerfacecolor='g', markersize=8))
plt.show()

# Créez des diagrammes en boîte horizontaux
plt.boxplot(data, vert=False)
plt.show()

# Créez plusieurs diagrammes en boîte sur une même figure
data1 = np.random.normal(0, 1, 50)
data2 = np.random.normal(1, 1, 50)
data3 = np.random.normal(2, 1, 50)

plt.boxplot([data1, data2, data3])
plt.show()
```
