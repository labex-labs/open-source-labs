# Gorutinas

El problema que se debe resolver en este desafío es crear y ejecutar gorutinas para ejecutar funciones concurrentemente.

## Requisitos

- La función `f` debe imprimir su cadena de entrada y una variable contador tres veces.
- La función `main` debe llamar a la función `f` de forma síncrona e imprimir "directo" y una variable contador tres veces.
- La función `main` debe llamar a la función `f` de forma asíncrona utilizando una gorutina e imprimir "gorutina" y una variable contador tres veces.
- La función `main` debe iniciar una gorutina para ejecutar una función anónima que imprima un mensaje.
- La función `main` debe esperar a que las gorutinas terminen de ejecutarse antes de imprimir "hecho".

## Ejemplo

```sh
# Cuando ejecutamos este programa, primero vemos la salida
# de la llamada bloqueante, luego la salida de las dos
# gorutinas. La salida de las gorutinas puede estar intercalada,
# porque las gorutinas se están ejecutando concurrentemente por
# el entorno de ejecución de Go.
$ go run goroutines.go
direct : 0
direct : 1
direct : 2
goroutine : 0
going
goroutine : 1
goroutine : 2
hecho

# A continuación, veremos un complemento a las gorutinas en
# los programas concurrentes de Go: los canales.
```
