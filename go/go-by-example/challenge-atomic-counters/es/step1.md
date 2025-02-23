# Contadores atómicos

El problema consiste en incrementar un contador exactamente 1000 veces utilizando 50 gorutinas y el paquete `sync/atomic`.

## Requisitos

- Utilizar el paquete `sync/atomic` para incrementar el contador.
- Utilizar un WaitGroup para esperar a que todas las gorutinas terminen su trabajo.

## Ejemplo

```sh
# Esperamos obtener exactamente 50.000 operaciones. Si hubiéramos
# utilizado el `ops++` no atómico para incrementar el contador,
# probablemente obtendríamos un número diferente, que variaría
# entre ejecuciones, porque las gorutinas se interpondrían
# entre sí. Además, obtendríamos errores de carrera de datos
# al ejecutar con la bandera `-race`.
$ go run atomic-counters.go
ops: 50000

# A continuación veremos los mutexes, otra herramienta para
# la gestión del estado.
```
