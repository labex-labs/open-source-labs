# Créer un objet Timer

Créer un nouvel objet Timer. Réglez l'intervalle sur 100 millisecondes (1000 est la valeur par défaut) et indiquez au timer quelle fonction devrait être appelée.

```python
timer = fig.canvas.new_timer(interval=100)
timer.add_callback(update_title, ax)
```
