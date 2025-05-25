# Converter texto para RGBA

Para converter texto em uma imagem, vamos desenhá-lo em uma figura vazia e transparente, salvar a figura em um buffer temporário e, em seguida, carregar o buffer usando `plt.imread`.

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
