# Основы журналирования

Создайте объект журналировщика.

```python
log = logging.getLogger(name)   # name - это строка
```

Вывод сообщений журнала.

```python
log.critical(message [, args])
log.error(message [, args])
log.warning(message [, args])
log.info(message [, args])
log.debug(message [, args])
```

_Каждый метод представляет собой разный уровень серьезности._

Все они создают отформатированное сообщение журнала. `args` используется с оператором `%` для создания сообщения.

```python
logmsg = message % args # Записывается в журнал
```
