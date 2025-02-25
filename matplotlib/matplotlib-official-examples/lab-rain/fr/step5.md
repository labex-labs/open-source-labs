# Créer l'animation

Enfin, nous allons créer l'animation en utilisant l'objet `FuncAnimation`, en passant la figure, la fonction de mise à jour, l'intervalle entre les trames en millisecondes et le nombre de trames à enregistrer.

```python
animation = FuncAnimation(fig, update, interval=10, save_count=100)
plt.show()
```
