# Testando com Vários Cenários de Data

Para entender melhor como nossa função `months_diff` funciona com diferentes cenários de data, vamos criar um arquivo de teste separado. Essa abordagem é comum no desenvolvimento de software para verificar se nosso código funciona como esperado.

Crie um novo arquivo chamado `month_diff_test.py` no diretório `/home/labex/project`:

```python
from datetime import date
from month_difference import months_diff

# Test scenario 1: Dates in the same month
date1 = date(2023, 5, 5)
date2 = date(2023, 5, 25)
print(f"Same month: {months_diff(date1, date2)} month(s)")

# Test scenario 2: Consecutive months
date3 = date(2023, 6, 28)
date4 = date(2023, 7, 15)
print(f"Consecutive months: {months_diff(date3, date4)} month(s)")

# Test scenario 3: Dates crossing year boundary
date5 = date(2023, 12, 20)
date6 = date(2024, 1, 10)
print(f"Across years: {months_diff(date5, date6)} month(s)")

# Test scenario 4: Several months apart
date7 = date(2023, 3, 10)
date8 = date(2023, 9, 20)
print(f"Several months: {months_diff(date7, date8)} month(s)")

# Test scenario 5: Dates in reverse order (negative result)
print(f"Reverse order: {months_diff(date8, date7)} month(s)")

# Test scenario 6: Exact multiples of 30 days
date9 = date(2023, 1, 1)
date10 = date(2023, 1, 31)  # 30 days
date11 = date(2023, 3, 2)   # 60 days
print(f"30 days exactly: {months_diff(date9, date10)} month(s)")
print(f"60 days exactly: {months_diff(date9, date11)} month(s)")
```

Salve este arquivo e execute-o:

```bash
python3 ~/project/month_diff_test.py
```

Você deve ver uma saída semelhante a:

```
Same month: 1 month(s)
Consecutive months: 1 month(s)
Across years: 1 month(s)
Several months: 7 month(s)
Reverse order: -7 month(s)
30 days exactly: 1 month(s)
60 days exactly: 2 month(s)
```

Vamos analisar esses resultados:

1.  **Mesmo mês**: Mesmo dentro do mesmo mês, nossa função retorna 1 mês. Isso ocorre porque mesmo um mês parcial é contado como um mês inteiro.

2.  **Meses consecutivos**: Para datas em meses consecutivos, a função retorna 1 mês.

3.  **Atravessando anos**: Para datas que cruzam a fronteira do ano, a função ainda calcula corretamente.

4.  **Vários meses**: Para datas que estão separados por vários meses, a função calcula o número apropriado de meses.

5.  **Ordem inversa**: Quando a data final é anterior à data inicial, obtemos um resultado negativo, o que faz sentido para cenários como calcular o tempo restante.

6.  **Múltiplos exatos**: Para exatamente 30 dias, obtemos 1 mês. Para 60 dias, obtemos 2 meses. Isso confirma que nossa função funciona como esperado com múltiplos exatos de nossa definição de mês.

Nossa função `months_diff` lida com todos esses casos de teste corretamente de acordo com nossa definição de um mês como 30 dias.
