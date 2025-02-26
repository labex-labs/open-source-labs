# Capturando excepciones

En lugar de detenerse con datos incorrectos, modifique el código para emitir un mensaje de advertencia en su lugar. El resultado final debe ser una lista de las filas que se convirtieron con éxito. Por ejemplo:

```python
>>> port = read_csv_as_dicts('missing.csv', types=[str, int, float])
Row 4: Bad row: ['C', '', '53.08']
Row 7: Bad row: ['DIS', '50', 'N/A']
Row 8: Bad row: ['GE', '', '37.23']
Row 13: Bad row: ['INTC', '', '21.84']
Row 17: Bad row: ['MCD', '', '51.11']
Row 19: Bad row: ['MO', '', '70.09']
Row 22: Bad row: ['PFE', '', '26.40']
Row 26: Bad row: ['VZ', '', '42.92']
>>> len(port)
20
>>>
```

Nota: Realizar este cambio puede ser un poco complicado debido a su uso previo de la función integrada `map()`. Es posible que tenga que abandonar ese enfoque ya que no hay forma fácil de capturar y manejar excepciones en `map()`.
