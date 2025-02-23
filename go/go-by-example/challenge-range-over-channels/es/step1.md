# Iteración sobre canales

Debes escribir una función que tome un canal de enteros y devuelva la suma de todos los enteros recibidos a través del canal.

## Requisitos

- La función debe llamarse `sumInts`.
- La función debe tomar un único parámetro de tipo `chan int`.
- La función debe devolver un único valor entero.
- No se permite utilizar ningún bucle o recursión dentro del cuerpo de la función.
- No se permite utilizar ningún paquete externo.

## Ejemplo

```sh
$ go run range-over-channels.go
uno
dos

# Este ejemplo también mostró que es posible cerrar
# un canal no vacío pero aún así recibir los valores restantes.
```
