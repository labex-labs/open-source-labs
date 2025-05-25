# Criar a Figura e os Eixos

Precisamos criar a figura e os eixos para o código de barras. Definiremos o tamanho da figura como um múltiplo do número de pontos de dados e desativaremos todos os eixos.

```python
fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
ax.set_axis_off()
```
