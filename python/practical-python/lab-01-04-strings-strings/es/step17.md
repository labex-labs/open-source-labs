# Ejercicio 1.18: Expresiones regulares

Una limitación de las operaciones básicas de cadenas es que no admiten ningún tipo de coincidencia de patrones avanzada. Para eso, debes recurrir al módulo `re` de Python y a las expresiones regulares. El manejo de expresiones regulares es un tema amplio, pero aquí hay un ejemplo corto:

```python
>>> text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
>>> # Encuentra todas las ocurrencias de una fecha
>>> import re
>>> re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']
>>> # Reemplaza todas las ocurrencias de una fecha con texto de reemplazo
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'
>>>
```

Para obtener más información sobre el módulo `re`, consulte la documentación oficial en [https://docs.python.org/library/re.html](https://docs.python.org/3/library/re.html).
