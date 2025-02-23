# Contrôle de la position et du style du texte

Nous pouvons également contrôler la position et le style du texte dans notre graphique Matplotlib. Essayez d'ajouter le code suivant à votre script :

```python
plt.text(2, 8, "Top Left", fontsize=12, color='red')
plt.text(8, 8, "Top Right", fontsize=12, color='blue')
plt.text(2, 2, "Bottom Left", fontsize=12, color='green')
plt.text(8, 2, "Bottom Right", fontsize=12, color='purple')
```

Cela ajoutera quatre éléments de texte à notre graphique, chacun avec une couleur, une taille de police et une position différentes.
