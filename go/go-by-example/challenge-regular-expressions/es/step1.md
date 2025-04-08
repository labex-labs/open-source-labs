# Expresiones regulares

El desafío requiere que completes el código para realizar varias tareas relacionadas con expresiones regulares en Golang.

## Requisitos

- Utiliza el paquete `regexp` para realizar tareas relacionadas con expresiones regulares.
- Utiliza `MatchString` para probar si un patrón coincide con una cadena.
- Utiliza `Compile` para optimizar una estructura `Regexp`.
- Utiliza `MatchString` para probar una coincidencia como `Compile`.
- Utiliza `FindString` para encontrar la coincidencia de la expresión regular.
- Utiliza `FindStringIndex` para encontrar la primera coincidencia y devolver los índices de inicio y fin de la coincidencia en lugar del texto coincidente.
- Utiliza `FindStringSubmatch` para devolver información tanto para `p([a-z]+)ch` como para `([a-z]+)`.
- Utiliza `FindStringSubmatchIndex` para devolver información sobre los índices de coincidencias y subcoincidencias.
- Utiliza `FindAllString` para encontrar todas las coincidencias de una expresión regular.
- Utiliza `FindAllStringSubmatchIndex` para aplicarse a todas las coincidencias en la entrada, no solo a la primera.
- Utiliza `Match` para probar una coincidencia con argumentos de `[]byte` y eliminar `String` del nombre de la función.
- Utiliza `MustCompile` para crear variables globales con expresiones regulares.
- Utiliza `ReplaceAllString` para reemplazar subconjuntos de cadenas con otros valores.
- Utiliza `ReplaceAllFunc` para transformar el texto coincidente con una función dada.

## Ejemplo

```sh

# Para una referencia completa sobre expresiones regulares de Go consulta
# la documentación del paquete [`regexp`](https://pkg.go.dev/regexp).
```
