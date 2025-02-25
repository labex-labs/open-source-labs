# Configurar el escritor

Necesitamos configurar el escritor que se utilizará para escribir los marcos en un archivo. Establecemos los fotogramas por segundo (fps) y agregamos metadatos como el título, el artista y el comentario.

```python
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)
```
