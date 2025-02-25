# Créer un graphique en barres

Matplotlib peut également créer des graphiques en barres. Voici un exemple :

```python
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 1, 9, 4]

plt.bar(x, y)
plt.xlabel('Catégorie')
plt.ylabel('Valeur')
plt.title('Graphique en barres')
plt.show()
```
