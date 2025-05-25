# Criar os Objetos de Texto Subsequentes

O próximo passo é criar os objetos de texto subsequentes usando `~.Axes.annotate`. Esta função permite posicionar o objeto de texto em relação ao objeto de texto anterior. O código a seguir cria três objetos de texto que são posicionados à direita do objeto de texto anterior.

```python
text = ax.annotate(
    " says,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # custom properties
text = ax.annotate(
    " hello", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # custom properties
text = ax.annotate(
    " world!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # custom properties
```
