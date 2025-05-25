# Média (Average)

Escreva uma função chamada `average` que recebe dois ou mais números e retorna sua média. Sua função deve seguir estas diretrizes:

- Use `sum()` para somar todos os `args` fornecidos, dividindo por `len()`.
- A função deve ser capaz de lidar com qualquer número de argumentos.
- A função deve retornar um `float`.

```python
def average(*args):
  return sum(args, 0.0) / len(args)
```

```python
average(*[1, 2, 3]) # 2.0
average(1, 2, 3) # 2.0
```
