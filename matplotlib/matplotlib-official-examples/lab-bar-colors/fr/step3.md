# Créer le graphique en barres

Maintenant, nous pouvons créer le graphique en barres à l'aide des données que nous avons définies dans l'Étape 2. Nous utiliserons la méthode `bar()` du module `pyplot` de Matplotlib pour créer le graphique. Nous passerons également les paramètres `label` et `color` pour contrôler respectivement les entrées de légende et les couleurs des barres. Le code suivant montre comment créer le graphique en barres :

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')
plt.show()
```
