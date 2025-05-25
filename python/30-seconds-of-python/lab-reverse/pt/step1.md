# Função para Inverter Lista

Escreva uma função Python chamada `reverse(itr)` que recebe uma lista ou uma string como argumento e retorna uma nova lista ou string que contém os elementos ou caracteres em ordem inversa.

Sua função deve ter os seguintes requisitos:

- A função deve ser chamada `reverse`
- A função deve receber um único argumento, que é uma lista ou uma string
- A função deve retornar uma nova lista ou string que contém os elementos ou caracteres em ordem inversa
- A função não deve modificar a lista ou string original

```python
def reverse(itr):
  return itr[::-1]
```

```python
reverse([1, 2, 3]) # [3, 2, 1]
reverse('snippet') # 'teppins'
```
