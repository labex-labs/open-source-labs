# Graficar los datos utilizando la subclase de figura personalizada

Utilice la función `plt.figure()` para graficar los datos utilizando la subclase de figura personalizada `WatermarkFigure`. En este ejemplo, agregaremos el texto de la marca de agua "borrador" a la trama.

```python
plt.figure(FigureClass=WatermarkFigure, watermark='draft')
plt.plot(x, y)
```
