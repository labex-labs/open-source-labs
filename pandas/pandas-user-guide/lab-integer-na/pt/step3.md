# Realizando Operações com Arrays de Inteiros Anuláveis

Você pode realizar várias operações com arrays de inteiros anuláveis, como operações aritméticas, comparações e fatiamento (slicing).

```python
# Criar um Series com tipo de inteiro anulável
s = pd.Series([1, 2, None], dtype="Int64")

# Realizar operação aritmética
s_plus_one = s + 1 # adiciona 1 a cada elemento no series

# Realizar comparação
comparison = s == 1 # verifica se cada elemento no series é igual a 1

# Realizar operação de fatiamento (slicing)
sliced = s.iloc[1:3] # seleciona o segundo e terceiro elementos no series
```
