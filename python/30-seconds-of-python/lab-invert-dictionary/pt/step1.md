# Inverter um Dicionário

Escreva uma função Python chamada `invert_dictionary(obj)` que recebe um dicionário `obj` como argumento e retorna um novo dicionário com as chaves e os valores invertidos. O dicionário de entrada `obj` terá valores únicos e _hashable_ (que podem ser usados como chaves de um dicionário). O dicionário de saída deve ter as mesmas chaves do dicionário de entrada, mas os valores devem ser as chaves do dicionário de entrada.

Você deve usar `dictionary.items()` em combinação com uma _list comprehension_ (compreensão de lista) para criar o novo dicionário.

```python
def invert_dictionary(obj):
  return { value: key for key, value in obj.items() }
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: 'Peter', 11: 'Isabel', 9: 'Anna' }
```
