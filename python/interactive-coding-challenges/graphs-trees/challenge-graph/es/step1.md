# Gráfico

## Problema

Implementar un gráfico que satisfaga los siguientes requisitos:

### Requisitos

- El gráfico puede ser dirigido o no dirigido.
- Las aristas pueden tener pesos.
- El gráfico puede tener ciclos.
- Si intentamos agregar un nodo que ya existe, simplemente no hacemos nada.
- Si intentamos eliminar un nodo que no existe, simplemente no hacemos nada.
- Podemos asumir que este es un gráfico conexo.
- Podemos asumir que las entradas son válidas.
- Podemos asumir que esto cabe en memoria.

## Uso de ejemplo

Entrada:

```
graph.add_edge(0, 1, 5)
graph.add_edge(0, 5, 2)
graph.add_edge(1, 2, 3)
graph.add_edge(2, 3, 4)
graph.add_edge(3, 4, 5)
graph.add_edge(3, 5, 6)
graph.add_edge(4, 0, 7)
graph.add_edge(5, 4, 8)
graph.add_edge(5, 2, 9)
```

Resultado:

- Los nodos `0`, `1`, `2`, `3`, `4` y `5` están conectados con los pesos especificados.

Nota:

- La clase `Graph` se usará como componente básico para desafíos de gráfico más complejos.
