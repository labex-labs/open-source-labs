# Cópias rasas (Shallow copies)

Listas e dicionários têm métodos para copiar.

```python
>>> a = [2,3,[100,101],4]
>>> b = list(a) # Make a copy
>>> a is b
False
```

É uma nova lista, mas os itens da lista são compartilhados.

```python
>>> a[2].append(102)
>>> b[2]
[100,101,102]
>>>
>>> a[2] is b[2]
True
>>>
```

Por exemplo, a lista interna `[100, 101, 102]` está sendo compartilhada. Isso é conhecido como uma cópia rasa (shallow copy). Aqui está uma imagem.

![Shallow copy](../assets/shallow.png)
