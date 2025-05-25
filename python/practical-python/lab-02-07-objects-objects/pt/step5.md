# Identidade e Referências

Use o operador `is` para verificar se dois valores são exatamente o mesmo objeto.

```python
>>> a = [1,2,3]
>>> b = a
>>> a is b
True
>>>
```

`is` compara a identidade do objeto (um inteiro). A identidade pode ser obtida usando `id()`.

```python
>>> id(a)
3588944
>>> id(b)
3588944
>>>
```

Observação: É quase sempre melhor usar `==` para verificar objetos. O comportamento de `is` é frequentemente inesperado:

```python
>>> a = [1,2,3]
>>> b = a
>>> c = [1,2,3]
>>> a is b
True
>>> a is c
False
>>> a == c
True
>>>
```
