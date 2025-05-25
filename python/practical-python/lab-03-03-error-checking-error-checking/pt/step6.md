# Capturando Múltiplos Erros (Catching Multiple Errors)

Você pode capturar diferentes tipos de exceções usando múltiplos blocos `except`.

```python
try:
  ...
except LookupError as e:
  ...
except RuntimeError as e:
  ...
except IOError as e:
  ...
except KeyboardInterrupt as e:
  ...
```

Alternativamente, se as instruções para tratá-las forem as mesmas, você pode agrupá-las:

```python
try:
  ...
except (IOError,LookupError,RuntimeError) as e:
  ...
```
