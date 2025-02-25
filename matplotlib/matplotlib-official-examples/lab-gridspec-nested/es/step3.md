# Crear el gridspec interno

Ahora, crearemos el gridspec interno. Utilizaremos el método `GridSpecFromSubplotSpec` para crear un gridspec de 3 por 3 que será un subgráfico del gridspec externo.

```python
gs00 = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec=gs0[0])
```
