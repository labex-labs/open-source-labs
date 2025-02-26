# Bases del registro

Crea un objeto de registro.

```python
log = logging.getLogger(name)   # name es una cadena
```

Emisión de mensajes de registro.

```python
log.critical(message [, args])
log.error(message [, args])
log.warning(message [, args])
log.info(message [, args])
log.debug(message [, args])
```

_Cada método representa un nivel diferente de gravedad._

Todos ellos crean un mensaje de registro formateado. `args` se utiliza con el operador `%` para crear el mensaje.

```python
logmsg = message % args # Escrito en el registro
```
