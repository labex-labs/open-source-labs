# Mutabilidade de String

Strings são "imutáveis" (immutable) ou somente leitura. Uma vez criados, o valor não pode ser alterado.

```python
>>> s = 'Hello World'
>>> s[1] = 'a'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

**Todas as operações e métodos que manipulam dados de string, sempre criam novas strings.**
