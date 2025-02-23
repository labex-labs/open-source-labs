# Créer l'animation

Enfin, nous pouvons créer l'animation à l'aide de la classe `FuncAnimation`. Nous passerons les paramètres `fig`, `run`, `data_gen`, `init_func` et `interval` pour créer l'animation. Nous définirons également le paramètre `save_count` sur 100 pour vous assurer que seules les 100 dernières trames sont enregistrées.

```python
ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init,
                              save_count=100)
```
