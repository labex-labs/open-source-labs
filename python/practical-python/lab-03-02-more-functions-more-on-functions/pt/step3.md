# Prefira argumentos de palavra-chave (keyword arguments) para argumentos opcionais

Compare e contraste estes dois estilos de chamada diferentes:

```python
parse_data(data, False, True) # ?????

parse_data(data, ignore_errors=True)
parse_data(data, debug=True)
parse_data(data, debug=True, ignore_errors=True)
```

Na maioria dos casos, os argumentos de palavra-chave melhoram a clareza do código – especialmente para argumentos que servem como flags ou que estão relacionados a recursos opcionais.
