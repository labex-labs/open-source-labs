# Fundamentos de `Logging`

Crie um objeto logger.

```python
log = logging.getLogger(name)   # name is a string
```

Emitindo mensagens de log.

```python
log.critical(message [, args])
log.error(message [, args])
log.warning(message [, args])
log.info(message [, args])
log.debug(message [, args])
```

_Cada método representa um nível diferente de severidade._

Todos eles criam uma mensagem de log formatada. `args` é usado com o operador `%` para criar a mensagem.

```python
logmsg = message % args # Written to the log
```
