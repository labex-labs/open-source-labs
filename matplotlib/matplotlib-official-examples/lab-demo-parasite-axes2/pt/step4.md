# Plotar os Dados

Plotaremos três conjuntos de dados no mesmo gráfico: Densidade (Density), Temperatura (Temperature) e Velocidade (Velocity). Usaremos a função `plot()` para plotar os dados.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Temperature")
p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")
```
