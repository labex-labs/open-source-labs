# Mutexes

El problema que se debe resolver en este desafío es incrementar un contador nombrado en un bucle utilizando múltiples goroutines y asegurarse de que el acceso al contador esté sincronizado.

## Requisitos

- Utilizar una estructura `Container` para almacenar un mapa de contadores.
- Utilizar un `Mutex` para sincronizar el acceso al mapa `counters`.
- La estructura `Container` debe tener un método `inc` que tome una cadena `name` e incremente el contador correspondiente en el mapa `counters`.
- El método `inc` debe bloquear el mutex antes de acceder al mapa `counters` y desbloquearlo al final de la función utilizando una declaración `defer`.
- Utilizar la estructura `sync.WaitGroup` para esperar a que las goroutines terminen.
- Utilizar la función `fmt.Println` para imprimir el mapa `counters`.

## Ejemplo

```sh
# Ejecutar el programa muestra que los contadores
# se actualizan como se esperaba.
$ go run mutexes.go
map[a:20000 b:10000]

# A continuación, veremos cómo implementar esta misma tarea
# de gestión de estado utilizando solo goroutines y canales.

```
