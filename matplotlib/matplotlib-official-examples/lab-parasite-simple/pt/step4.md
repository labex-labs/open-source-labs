# Adicionando Dados

Adicionaremos os dados ao gráfico usando a função `plot`. Atribuiremos cada linha a uma variável para que possamos referenciá-la mais tarde.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par.plot([0, 1, 2], [0, 3, 2], label="Temperature")
```
