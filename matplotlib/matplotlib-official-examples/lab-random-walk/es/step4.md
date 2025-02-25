# Generar paseos aleatorios

Generamos 40 paseos aleatorios con 30 pasos cada uno utilizando la función `random_walk()` definida anteriormente. Guardamos todos los paseos aleatorios en una lista llamada `walks`.

```python
# Data: 40 random walks as (num_steps, 3) arrays
num_steps = 30
walks = [random_walk(num_steps) for index in range(40)]
```
