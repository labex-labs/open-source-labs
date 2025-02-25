# Crear objeto PathPatch

En este paso, creamos un objeto `PathPatch` utilizando el objeto de ruta que creamos en el paso anterior. Este objeto se utiliza para rellenar el área encerrada por la ruta. También podemos establecer el color y la transparencia del recuadro.

```python
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
```
