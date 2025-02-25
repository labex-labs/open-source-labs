# Cargar la fuente

En este paso, cargaremos la fuente con la que trabajaremos. Usaremos una fuente que viene con Matplotlib.

```python
font = ft.FT2Font(
    os.path.join(matplotlib.get_data_path(),
                 'fonts/ttf/DejaVuSans-Oblique.ttf'))
```
