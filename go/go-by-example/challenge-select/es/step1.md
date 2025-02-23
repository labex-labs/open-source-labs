# Select

En este desafío, se te dan dos canales, `c1` y `c2`, que recibirán un valor después de cierto tiempo. Tu tarea es utilizar `select` para esperar simultáneamente ambos valores, imprimiendo cada uno a medida que llega.

## Requisitos

- Debes utilizar la declaración `select` para esperar en ambos canales.
- Debes imprimir el valor recibido de cada canal a medida que llega.

## Ejemplo

```sh
# Recibimos los valores `"uno"` y luego `"dos"` como
# se esperaba.
$ time go run select.go
recibido uno
recibido dos

# Tenga en cuenta que el tiempo total de ejecución es solo ~2 segundos
# ya que las dos `Sleeps` de 1 y 2 segundos se ejecutan
# concurrentemente.
real 0m2.245s
```
