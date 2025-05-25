# Exercício 1.18: Expressões Regulares

Uma limitação das operações básicas de string é que elas não suportam nenhum tipo de correspondência de padrão avançada. Para isso, você precisa recorrer ao módulo `re` do Python e às expressões regulares. O tratamento de expressões regulares é um tópico extenso, mas aqui está um exemplo curto:

```python
>>> text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
>>> # Find all occurrences of a date
>>> import re
>>> re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']
>>> # Replace all occurrences of a date with replacement text
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'
>>>
```

Para mais informações sobre o módulo `re`, consulte a documentação oficial em [https://docs.python.org/library/re.html](https://docs.python.org/3/library/re.html).
