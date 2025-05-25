# Transformar Coordenadas

O próximo passo é transformar as coordenadas dos dados e da exibição. Usaremos o método `ax.transData` para transformar as coordenadas dos dados e o sistema de coordenadas `figure pixels` para transformar as coordenadas da exibição.

```python
xdata, ydata = 5, 0
xdisplay, ydisplay = ax.transData.transform((xdata, ydata))
```
