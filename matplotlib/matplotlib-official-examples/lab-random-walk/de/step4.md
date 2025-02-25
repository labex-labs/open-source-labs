# Generieren von Zufallswalks

Wir generieren 40 Zufallswalks mit jeweils 30 Schritten mithilfe der zuvor definierten Funktion `random_walk()`. Wir speichern alle Zufallswalks in einer Liste namens `walks`.

```python
# Data: 40 random walks as (num_steps, 3) arrays
num_steps = 30
walks = [random_walk(num_steps) for index in range(40)]
```
