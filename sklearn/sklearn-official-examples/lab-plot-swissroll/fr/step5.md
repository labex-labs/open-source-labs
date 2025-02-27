# Générer l'ensemble de données Swiss-Hole

Nous générons l'ensemble de données Swiss-Hole en ajoutant un trou à l'ensemble de données Swiss Roll en utilisant le paramètre `hole=True` dans la fonction `make_swiss_roll()`.

```python
sh_points, sh_color = datasets.make_swiss_roll(n_samples=1500, hole=True, random_state=0)
```
