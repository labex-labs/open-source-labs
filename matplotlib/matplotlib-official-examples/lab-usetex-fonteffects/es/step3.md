# Definir la función de fuente

En este paso, definiremos una función que establece la fuente. Esta función toma el nombre de una fuente como argumento y devuelve una cadena que establece la fuente al nombre especificado.

```python
def setfont(font):
    return rf'\font\a {font} at 14pt\a '
```
