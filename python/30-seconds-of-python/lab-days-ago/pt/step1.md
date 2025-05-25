# Dias Atrás

Sua tarefa é escrever uma função chamada `days_ago(n)` que recebe um inteiro `n` como argumento e retorna a data de `n` dias atrás a partir de hoje.

Para resolver este problema, você precisa usar a classe `date` do módulo `datetime` para obter a data atual e a classe `timedelta` para subtrair `n` dias da data atual.

```python
from datetime import timedelta, date

def days_ago(n):
  return date.today() - timedelta(n)
```

```python
days_ago(5) # date(2020, 10, 23)
```
