# Plotar os dados usando a subclasse de figura personalizada

Use a função `plt.figure()` para plotar os dados usando a subclasse de figura personalizada `WatermarkFigure`. Neste exemplo, adicionaremos o texto da marca d'água "draft" ao gráfico.

```python
plt.figure(FigureClass=WatermarkFigure, watermark='draft')
plt.plot(x, y)
```
