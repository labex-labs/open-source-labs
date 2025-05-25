# Relançando uma Exceção (Reraising an Exception)

Use `raise` para propagar um erro capturado.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
    raise
```

Isso permite que você tome uma ação (por exemplo, logging) e passe o erro para quem chamou a função.
