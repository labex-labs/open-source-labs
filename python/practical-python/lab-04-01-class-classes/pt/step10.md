# Exercício 4.4: Usando sua classe

Modifique a função `read_portfolio()` no programa `report.py` para que ela leia um portfólio em uma lista de instâncias de `Stock`, como mostrado no Exercício 4.3. Depois de fazer isso, corrija todo o código em `report.py` e `pcost.py` para que ele funcione com instâncias de `Stock` em vez de dicionários.

Dica: Você não deve precisar fazer grandes alterações no código. Você estará principalmente alterando o acesso a dicionários, como `s['shares']`, para `s.shares`.

Você deve ser capaz de executar suas funções da mesma forma que antes:

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```
