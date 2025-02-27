# Generar el conjunto de datos Swiss-Hole

Generamos el conjunto de datos Swiss-Hole agregando un agujero al conjunto de datos Swiss Roll utilizando el parámetro `hole=True` en la función `make_swiss_roll()`.

```python
sh_points, sh_color = datasets.make_swiss_roll(n_samples=1500, hole=True, random_state=0)
```
