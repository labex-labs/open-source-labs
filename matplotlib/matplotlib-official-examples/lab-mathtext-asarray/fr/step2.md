# Convertir le texte en RGBA

Pour convertir du texte en image, nous allons le dessiner sur une figure vide et transparente, enregistrer la figure dans un tampon temporaire, puis charger le tampon à l'aide de `plt.imread`.

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
