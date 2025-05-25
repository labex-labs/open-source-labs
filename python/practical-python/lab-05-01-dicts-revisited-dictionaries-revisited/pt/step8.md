# Lendo Atributos

Suponha que você leia um atributo em uma instância.

```python
x = obj.name
```

O atributo pode existir em dois lugares:

- Dicionário de instância local.
- Dicionário da classe.

Ambos os dicionários devem ser verificados. Primeiro, verifique no `__dict__` local. Se não for encontrado, procure em `__dict__` da classe através de `__class__`.

```python
>>> s = Stock(...)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>>
```

Este esquema de busca é como os membros de uma _classe_ são compartilhados por todas as instâncias.
