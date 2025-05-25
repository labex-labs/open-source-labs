# Criar um gráfico de barras polar

Criaremos um gráfico de barras polar usando o parâmetro `projection='polar'`.

```python
ax = plt.subplot(projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)
```
