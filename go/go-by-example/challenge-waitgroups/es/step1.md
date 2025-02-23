# waitgroups

El problema que se debe resolver en este desafío es lanzar varias gorutinas e incrementar el contador del WaitGroup para cada una. Luego, debemos esperar a que terminen todas las gorutinas lanzadas.

## Requisitos

- Conocimientos básicos de Golang.
- Comprensión de la concurrencia en Golang.
- Familiaridad con el paquete `sync`.

## Ejemplo

```sh
$ go run waitgroups.go
Worker 5 starting
Worker 3 starting
Worker 4 starting
Worker 1 starting
Worker 2 starting
Worker 4 done
Worker 1 done
Worker 2 done
Worker 5 done
Worker 3 done

# El orden en que los workers se inician y terminan
# es probable que sea diferente para cada invocación.
```
