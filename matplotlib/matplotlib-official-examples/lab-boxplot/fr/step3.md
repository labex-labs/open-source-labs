# Diagramme en boîte par défaut

Nous commencerons par créer un diagramme en boîte par défaut pour visualiser les données. Nous utiliserons la fonction `boxplot()` de Matplotlib et passer les données et les étiquettes en tant qu'arguments. Nous définirons également le titre du graphique à l'aide de la fonction `set_title()`.

```python
fig, ax = plt.subplots()
ax.boxplot(data, labels=labels)
ax.set_title('Default Box Plot')
plt.show()
```
