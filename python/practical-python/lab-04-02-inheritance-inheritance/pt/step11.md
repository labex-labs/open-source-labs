# Herança Múltipla

Você pode herdar de múltiplas classes, especificando-as na definição da classe.

```python
class Mother:
    ...

class Father:
    ...

class Child(Mother, Father):
    ...
```

A classe `Child` herda características de ambos os pais. Existem alguns detalhes bastante complicados. Não faça isso a menos que saiba o que está fazendo. Algumas informações adicionais serão fornecidas na próxima seção, mas não vamos utilizar herança múltipla neste curso.

Um uso importante da herança é na escrita de código que se destina a ser estendido ou personalizado de várias maneiras - especialmente em bibliotecas ou frameworks. Para ilustrar, considere a função `print_report()` em seu programa `report.py`. Ela deve se parecer com isto:

```python
def print_report(reportdata):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)
```

Quando você executar seu programa de relatório, você deve obter uma saída como esta:

```python
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
```
