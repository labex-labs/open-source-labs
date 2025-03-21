# Упражнение 1.18: Регулярные выражения

Одна из ограниченностей базовых операций со строками заключается в том, что они не поддерживают никакого вида продвинутого сопоставления шаблонов. Для этого вам нужно обратиться к модулю `re` в Python и регулярным выражениям. Работа с регулярными выражениями - большая тема, но вот простой пример:

```python
>>> text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
>>> # Найти все вхождения даты
>>> import re
>>> re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']
>>> # Заменить все вхождения даты на текст замены
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'
>>>
```

Для получения дополнительной информации о модуле `re` обратитесь к официальной документации по адресу [https://docs.python.org/library/re.html](https://docs.python.org/3/library/re.html).
