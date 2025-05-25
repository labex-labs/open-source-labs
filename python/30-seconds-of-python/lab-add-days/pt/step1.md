# Adicionar Dias à Data

Escreva uma função `add_days(n, d)` que recebe dois argumentos:

- `n`: um inteiro representando o número de dias a adicionar (se positivo) ou subtrair (se negativo) da data fornecida.
- `d`: um argumento opcional representando a data à qual os dias devem ser adicionados ou subtraídos. Se não for fornecido, a data atual deve ser usada.

A função deve retornar um objeto `datetime` representando a nova data após adicionar ou subtrair o número especificado de dias.

```python
from datetime import datetime, timedelta

def add_days(n, d = datetime.today()):
  return d + timedelta(n)
```

```python
from datetime import date

add_days(5, date(2020, 10, 25)) # date(2020, 10, 30)
add_days(-5, date(2020, 10, 25)) # date(2020, 10, 20)
```
