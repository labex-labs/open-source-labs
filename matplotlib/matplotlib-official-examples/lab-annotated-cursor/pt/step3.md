# Criar a classe AnnotatedCursor

Criamos uma nova classe `AnnotatedCursor` que herda de `matplotlib.widgets.Cursor` e demonstra a criação de novos widgets e seus retornos de chamada de eventos (event callbacks). A classe `AnnotatedCursor` é usada para criar um cursor em forma de cruz com um texto mostrando as coordenadas atuais.

```python
class AnnotatedCursor(Cursor):
    """
    A crosshair cursor like `~matplotlib.widgets.Cursor` with a text showing \
    the current coordinates.
    ...
    """
```
