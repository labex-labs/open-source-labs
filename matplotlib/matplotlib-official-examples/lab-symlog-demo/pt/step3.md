# Criar Gráficos

Agora que temos nossos dados, podemos criar nossos gráficos. Criaremos três subplots, cada um com uma escala de eixo `symlog` diferente.

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
```
