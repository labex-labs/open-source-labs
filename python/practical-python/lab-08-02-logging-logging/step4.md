# Logging Basics

Create a logger object.

```python
log = logging.getLogger(name)   # name is a string
```

Issuing log messages.

```python
log.critical(message [, args])
log.error(message [, args])
log.warning(message [, args])
log.info(message [, args])
log.debug(message [, args])
```

_Each method represents a different level of severity._

All of them create a formatted log message. `args` is used with the `%` operator to create the message.

```python
logmsg = message % args # Written to the log
```
