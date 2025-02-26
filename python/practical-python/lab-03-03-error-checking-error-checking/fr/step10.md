# Reprovoquer une exception

Utilisez `raise` pour propager une erreur capturée.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
    raise
```

Cela vous permet de prendre des mesures (par exemple, journalisation) et de transmettre l'erreur à l'appelant.
