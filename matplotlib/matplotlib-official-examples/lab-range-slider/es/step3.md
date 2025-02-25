# Crear el RangeSlider

Ahora crearemos el widget RangeSlider, que nos permitirá ajustar el umbral de la imagen. Crearemos un nuevo eje para el deslizador y lo agregaremos a la figura.

```python
slider_ax = fig.add_axes([0.20, 0.1, 0.60, 0.03])
slider = RangeSlider(slider_ax, "Threshold", img.min(), img.max())
```
