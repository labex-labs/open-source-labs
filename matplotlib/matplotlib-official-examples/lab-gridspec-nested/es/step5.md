# Crear otro gridspec interno

Ahora crearemos otro gridspec interno. Esta vez, utilizaremos el método `subgridspec` para crear un gridspec de 3 por 3 que será un subgráfico de la segunda columna del gridspec externo.

```python
gs01 = gs0[1].subgridspec(3, 3)
```
