# Crear los siguientes objetos de texto

El siguiente paso es crear los siguientes objetos de texto utilizando `~.Axes.annotate`. Esta función le permite posicionar el objeto de texto con respecto al objeto de texto anterior. El siguiente código crea tres objetos de texto que se posicionan a la derecha del objeto de texto anterior.

```python
text = ax.annotate(
    " dice,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="oro", weight="bold")  # propiedades personalizadas
text = ax.annotate(
    " hola", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="verde", style="italic")  # propiedades personalizadas
text = ax.annotate(
    " mundo!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="azul", family="serif")  # propiedades personalizadas
```
