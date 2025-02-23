# Grupos de Trabajadores

Implementa un grupo de trabajadores que reciba trabajos a través del canal `jobs` y envíe los resultados correspondientes a través del canal `results`. El grupo de trabajadores debe tener múltiples instancias concurrentes, y cada trabajador debe dormir durante un segundo por trabajo para simular una tarea costosa.

## Requisitos

- Utiliza goroutines y canales para implementar el grupo de trabajadores.
- El grupo de trabajadores debe tener múltiples instancias concurrentes.
- Cada trabajador debe dormir durante un segundo por trabajo para simular una tarea costosa.
- El grupo de trabajadores debe recibir trabajos a través del canal `jobs` y enviar los resultados correspondientes a través del canal `results`.

## Ejemplo

```sh
# Nuestro programa en ejecución muestra los 5 trabajos siendo ejecutados por
# varios trabajadores. El programa solo tarda aproximadamente 2 segundos
# a pesar de realizar aproximadamente 5 segundos de trabajo en total porque
# hay 3 trabajadores operando de manera concurrente.
$ time go run worker-pools.go
worker 1 started job 1
worker 2 started job 2
worker 3 started job 3
worker 1 finished job 1
worker 1 started job 4
worker 2 finished job 2
worker 2 started job 5
worker 3 finished job 3
worker 1 finished job 4
worker 2 finished job 5

real 0m2.358s
```
