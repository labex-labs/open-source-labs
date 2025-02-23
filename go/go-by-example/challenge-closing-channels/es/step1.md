# Cerrando canales

En este desafío, debes modificar el código dado para cerrar el canal `jobs` cuando ya no hay más trabajos para el trabajador. También debes utilizar el canal `done` para notificar cuando todos los trabajos hayan sido completados.

## Requisitos

- Utiliza un canal bufferizado `jobs` para comunicar el trabajo que se debe realizar desde la gorutina `main()` a una gorutina trabajadora.
- Utiliza un canal `done` para notificar cuando todos los trabajos hayan sido completados.
- Utiliza una gorutina trabajadora para recibir repetidamente de `jobs` con `j, more := <-jobs`.
- Utiliza la forma especial de recepción de dos valores para notificar en `done` cuando todos los trabajos hayan sido completados.
- Envía 3 trabajos al trabajador a través del canal `jobs`, luego cierra el canal.
- Utiliza el enfoque de [sincronización](channel-synchronization) para esperar a la trabajadora.

## Ejemplo

```sh
$ go run closing-channels.go
sent job 1
received job 1
sent job 2
received job 2
sent job 3
received job 3
sent all jobs
received all jobs

# La idea de los canales cerrados conduce naturalmente a nuestro siguiente
# ejemplo: `range` sobre canales.
```
