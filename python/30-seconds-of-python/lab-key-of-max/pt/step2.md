# Lidando com o Caso de Dicionário Vazio

Nossa função atual tem um problema: ela irá travar se o dicionário de entrada `d` estiver vazio. Vamos corrigir isso. Modifique `key_of_max.py` para que se pareça com isto:

```python
def key_of_max(d):
  """
  Retorna a chave associada ao valor máximo no dicionário 'd'.

  Se várias chaves compartilharem o valor máximo, qualquer uma delas pode ser retornada.
  """
  if not d:  # Verifica se o dicionário está vazio
      return None
  return max(d, key=d.get)
```

As linhas adicionadas fazem o seguinte:

- **`if not d:`**: Em Python, um dicionário vazio é considerado "falsy" (falso). Esta instrução `if` verifica se o dicionário `d` está vazio.
- **`return None`**: Se o dicionário estiver vazio, não há valor máximo, então retornamos `None`. Esta é uma maneira padrão de indicar a ausência de um valor em Python. Isso impede que a função `max()` levante um erro.

Este é um passo crucial na escrita de código robusto: sempre considere os casos de borda (edge cases)!
