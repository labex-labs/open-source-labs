# Métodos

El código proporcionado define un tipo de struct llamado `rect` con dos campos, `width` y `height`. Se definen dos métodos para este tipo de struct, `area` y `perim`. El método `area` calcula el área del rectángulo, y el método `perim` calcula el perímetro del rectángulo. La función principal llama a estos dos métodos y muestra sus resultados.

## Requisitos

- El método `area` debe tener un tipo de receptor de `*rect`.
- El método `perim` debe tener un tipo de receptor de `rect`.
- El método `area` debe devolver el área del rectángulo.
- El método `perim` debe devolver el perímetro del rectángulo.
- La función `main` debe llamar a ambos métodos y mostrar sus resultados.

## Ejemplo

```sh
$ go run methods.go
area: 50
perim: 30
area: 50
perim: 30

# A continuación, veremos el mecanismo de Go para agrupar y
# nombrar conjuntos relacionados de métodos: interfaces.
```
