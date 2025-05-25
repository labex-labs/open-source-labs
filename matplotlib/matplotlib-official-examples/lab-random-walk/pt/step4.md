# Gerar Passeios Aleatórios

Geramos 40 passeios aleatórios com 30 passos cada, usando a função `random_walk()` definida anteriormente. Armazenamos todos os passeios aleatórios em uma lista chamada `walks`.

```python
# Data: 40 random walks as (num_steps, 3) arrays
num_steps = 30
walks = [random_walk(num_steps) for index in range(40)]
```
