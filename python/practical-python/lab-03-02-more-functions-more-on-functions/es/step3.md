# Prefiera los argumentos de palabras clave para los argumentos opcionales

Compare y contraste estos dos diferentes estilos de llamada:

```python
parse_data(data, False, True) #?????

parse_data(data, ignore_errors=True)
parse_data(data, debug=True)
parse_data(data, debug=True, ignore_errors=True)
```

En la mayoría de los casos, los argumentos de palabras clave mejoran la claridad del código, especialmente para los argumentos que sirven como banderas o que están relacionados con características opcionales.
