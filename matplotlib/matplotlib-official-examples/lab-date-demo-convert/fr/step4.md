# Créez le graphique

Maintenant, nous pouvons créer le graphique à l'aide des dates et des valeurs de y. Nous allons tout d'abord créer un objet figure et d'axe à l'aide de la fonction subplots. Ensuite, nous traçons le graphique à l'aide de la fonction plot. Copiez et collez le code suivant :

```python
fig, ax = plt.subplots()
ax.plot(dates, y**2, 'o')
```
