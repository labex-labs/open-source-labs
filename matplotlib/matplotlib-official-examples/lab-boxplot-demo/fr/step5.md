# Ajoutez des étiquettes et des titres

Enfin, nous pouvons ajouter des étiquettes et des titres à notre diagramme en boîte pour le rendre plus informatif. Nous pouvons ajouter des étiquettes aux axes x et y, ainsi qu'un titre au tracé. Nous pouvons également changer la taille et le style de police des étiquettes et du titre. Voici un exemple de comment ajouter des étiquettes et des titres :

```python
plt.boxplot([data1, data2, data3])
plt.xlabel('Group')
plt.ylabel('Value')
plt.title('Comparison of Three Groups')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
```
