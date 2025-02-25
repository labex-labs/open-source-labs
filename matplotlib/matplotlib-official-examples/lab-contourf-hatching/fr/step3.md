# Plus simple tracé haché avec une barre de couleur

Dans cette étape, nous allons créer le tracé haché le plus simple avec une barre de couleur. Nous utiliserons la fonction `contourf` pour créer le graphe de courbes de niveau remplies et spécifier les hachures à l'aide du paramètre `hatches`.

```python
fig1, ax1 = plt.subplots()
cs = ax1.contourf(x, y, z, hatches=['-', '/', '\\', '//'],
                  cmap='gray', extend='both', alpha=0.5)
fig1.colorbar(cs)
```
