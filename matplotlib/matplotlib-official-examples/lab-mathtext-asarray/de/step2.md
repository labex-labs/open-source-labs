# Text in RGBA umwandeln

Um Text in ein Bild umzuwandeln, zeichnen wir ihn auf eine leere und transparente Figur, speichern die Figur in einem temporären Puffer und laden dann den Puffer mit `plt.imread` ein.

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
