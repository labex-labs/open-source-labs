# Pensamiento profundo

En este ejercicio, has escrito dos funciones, `read_csv_as_dicts()` y `read_csv_as_columns()`. Estas funciones presentan los datos al usuario de la misma manera. Por ejemplo:

```python
>>> data1 = read_csv_as_dicts('ctabus.csv', [str, str, str, int])
>>> len(data1)
577563
>>> data1[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data1[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>

>>> data2 = read_csv_as_columns('ctabus.csv', [str, str, str, int])
>>> len(data2)
577563
>>> data2[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data2[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>
```

De hecho, puedes usar cualquiera de las funciones en el código de análisis de datos de CTA que has escrito. Sin embargo, por debajo, están sucediendo cosas completamente diferentes. La función `read_csv_as_columns()` está almacenando los datos en una representación diferente. Está confiada en los protocolos de secuencia de Python (métodos mágicos) para presentarte la información de una manera más útil.

Esto es realmente parte de un concepto de programación mucho más amplio llamado "Abstracción de datos". Al escribir programas, la forma en que se presentan los datos es a menudo más importante que cómo se combinan realmente los datos por debajo del capó. Aunque estamos presentando los datos como una secuencia de diccionarios, hay mucha flexibilidad en cómo realmente sucede eso en los fondos. Esa es una idea poderosa y algo en lo que pensar cuando escribes tus propios programas.
