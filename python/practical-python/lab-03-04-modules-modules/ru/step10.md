# Поиск модулей

Python обращается к списку путей (`sys.path`), когда ищет модули.

```python
>>> import sys
>>> sys.path
[
  '',
  '/usr/local/lib/python36/python36.zip',
  '/usr/local/lib/python36',
...
]
```

Обычно первым в списке является текущая рабочая директория.
