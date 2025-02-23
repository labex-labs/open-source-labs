# Señales

En algunos casos, queremos que nuestros programas Go manejen inteligentemente las señales Unix. Por ejemplo, podemos querer que un servidor se detenga de manera adecuada cuando recibe un `SIGTERM`, o que una herramienta de línea de comandos deje de procesar la entrada si recibe un `SIGINT`.

## Requisitos

- Crear un canal bufferizado para recibir notificaciones de `os.Signal`.
- Registrar el canal para recibir notificaciones de señales específicas utilizando `signal.Notify`.
- Crear una goroutine para ejecutar una recepción bloqueante de señales.
- Imprimir la señal recibida y notificar al programa que puede finalizar.
- Esperar la señal esperada y luego salir.

## Ejemplo

```sh
# Cuando ejecutamos este programa, se bloqueará esperando una
# señal. Al presionar `ctrl-C` (que la terminal muestra como `^C`),
# podemos enviar una señal `SIGINT`, lo que hará que el programa imprima
# `interrupt` y luego salga.
$ go run signals.go
awaiting signal
^C
interrupt
exiting
```
