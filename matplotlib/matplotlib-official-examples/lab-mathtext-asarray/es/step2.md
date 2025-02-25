# Convertir texto a RGBA

Para convertir texto en una imagen, lo dibujaremos en una figura vacía y transparente, guardaremos la figura en un búfer temporal y luego cargaremos el búfer usando `plt.imread`.

```python
def text_to_rgba(s, *, dpi, **kwargs):
    fig = Figure(facecolor="none")
    fig.text(0, 0, s, **kwargs)
    with BytesIO() as buf:
        fig.savefig(buf, dpi=dpi, format="png", bbox_inches="tight", pad_inches=0)
        buf.seek(0)
        rgba = plt.imread(buf)
    return rgba
```
