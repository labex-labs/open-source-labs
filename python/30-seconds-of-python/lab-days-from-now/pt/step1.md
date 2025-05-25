# Dias a partir de agora

Escreva uma função `days_from_now(n)` que recebe um inteiro `n` como entrada e retorna a data de `n` dias a partir de hoje.

Para resolver este problema, você pode seguir estes passos:

1. Importe o módulo `datetime`.
2. Use o método `date.today()` para obter a data atual.
3. Use o método `timedelta` para adicionar `n` dias à data atual.
4. Retorne a nova data.

```python
from datetime import timedelta, date

def days_from_now(n):
  return date.today() + timedelta(n)
```

```python
days_from_now(5) # date(2020, 11, 02)
```
