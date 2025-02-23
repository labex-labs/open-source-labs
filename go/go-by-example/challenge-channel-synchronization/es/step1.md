# Sincronización de canales

El problema que se debe resolver en este desafío es crear una goroutine que realice alguna tarea y notifique a otra goroutine cuando haya terminado utilizando un canal.

## Requisitos

Para completar este desafío, necesitarás:

- Crear una función llamada `worker` que tome un canal de tipo `bool` como parámetro.
- Dentro de la función `worker`, realizar alguna tarea y luego enviar un valor al canal para notificar que la tarea ha terminado.
- En la función `main`, crear un canal de tipo `bool` con un tamaño de búfer de 1.
- Iniciar una goroutine que llame a la función `worker` y pase el canal como parámetro.
- Bloquear la función `main` hasta que se reciba un valor del canal.

## Ejemplo

```sh
$ go run channel-synchronization.go
working...done

# Si eliminas la línea `<- done` de este programa, el
# programa se cerrará antes de que la `worker` incluso
# comience.
```
