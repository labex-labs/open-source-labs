# Preenchendo os Gráficos de Caixa com Cores Personalizadas

Em seguida, preencheremos os gráficos de caixa com cores personalizadas. Criaremos uma lista de cores e usaremos um loop para preencher cada caixa com uma cor diferente.

```python
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
```
