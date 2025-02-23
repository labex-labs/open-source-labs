# Gorutinas con Estado

En la programación concurrente, es esencial sincronizar el acceso al estado compartido para evitar condiciones de carrera y corrupción de datos. Este desafío presenta un escenario en el que una sola gorutina posee el estado y otras gorutinas envían mensajes para leer o escribir el estado.

## Requisitos

- Utilizar canales para emitir solicitudes de lectura y escritura a la gorutina propietaria del estado.
- Utilizar structs `readOp` y `writeOp` para encapsular solicitudes y respuestas.
- Utilizar un mapa para almacenar el estado.
- Utilizar canales `resp` para indicar éxito y devolver valores.
- Utilizar el paquete `atomic` para contar operaciones de lectura y escritura.
- Utilizar el paquete `time` para agregar un retraso entre operaciones.

## Ejemplo

```sh
# Ejecutar nuestro programa muestra que el ejemplo de
# gestión de estado basado en gorutinas completa
# aproximadamente 80.000 operaciones en total.
$ go run stateful-goroutines.go
readOps: 71708
writeOps: 7177

# En este caso particular, el enfoque basado en gorutinas
# fue un poco más complejo que el basado en mutex. Sin
# embargo, puede ser útil en ciertos casos, por ejemplo,
# donde se involucren otros canales o cuando la gestión
# de múltiples mutexes sería propensa a errores. Deberías
# utilizar el enfoque que se sienta más natural,
# especialmente con respecto a la comprensión de la
# corrección de tu programa.
```
