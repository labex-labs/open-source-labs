# Capturar marcos y escribir en un archivo

Recorremos 100 iteraciones y generamos números aleatorios para las coordenadas x e y. Actualizamos los datos de la gráfica de línea y capturamos el marco usando el escritor. Finalmente, guardamos los marcos en un archivo.

```python
x0, y0 = 0, 0

with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(100):
        x0 += 0.1 * np.random.randn()
        y0 += 0.1 * np.random.randn()
        l.set_data(x0, y0)
        writer.grab_frame()
```
