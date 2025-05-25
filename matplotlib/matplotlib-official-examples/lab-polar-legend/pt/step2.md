# Criar uma Figura e Subplot

Em seguida, precisamos criar uma figura e um subplot para nosso gráfico. Usaremos o parâmetro `projection` de `add_subplot` para criar um gráfico polar.

```python
fig = plt.figure()
ax = fig.add_subplot(projection="polar", facecolor="lightgoldenrodyellow")
```
