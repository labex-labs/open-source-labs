# Canales

En este desafío, se te pide crear un nuevo canal y enviar un valor a través de él desde una nueva gorutina. Luego recibirás el valor del canal y lo imprimirás.

## Requisitos

- Debes utilizar la sintaxis `make(chan val-tipo)` para crear un nuevo canal.
- El canal debe ser tipado por los valores que transporta.
- Debes utilizar la sintaxis `canal <-` para enviar un valor al canal.
- Debes utilizar la sintaxis `<-canal` para recibir un valor del canal.
- Debes utilizar una nueva gorutina para enviar el valor al canal.

## Ejemplo

```sh
# Cuando ejecutamos el programa, el mensaje "ping" se
# pasa con éxito de una gorutina a otra a través de
# nuestro canal.
$ go run channels.go
ping

# Por defecto, los envíos y recepciones se bloquean hasta
# que tanto el emisor como el receptor estén listos. Esta
# propiedad nos permitió esperar al final de nuestro
# programa el mensaje "ping" sin tener que utilizar ninguna
# otra sincronización.
```
