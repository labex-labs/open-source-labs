# Пространства имен

Модуль - это коллекция именованных значений и иногда называется _пространством имен_. Имена представляют собой все глобальные переменные и функции, определенные в исходном файле. После импорта имя модуля используется в качестве префикса. Отсюда и _пространство имен_.

```python
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```

Имя модуля напрямую связано с именем файла (foo -> foo.py).
