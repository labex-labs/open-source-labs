# Exercício 4.8: Juntando tudo

Modifique o programa `report.py` para que a função `portfolio_report()` aceite um argumento opcional que especifica o formato de saída. Por exemplo:

```python
>>> report.portfolio_report('portfolio.csv', 'prices.csv', 'txt')
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

Modifique o programa principal para que um formato possa ser fornecido na linha de comando:

```bash
$ python3 report.py portfolio.csv prices.csv csv
Name,Shares,Price,Change
AA,100,9.22,-22.98
IBM,50,106.28,15.18
CAT,150,35.46,-47.98
MSFT,200,20.89,-30.34
GE,95,13.48,-26.89
MSFT,50,20.89,-44.21
IBM,100,106.28,35.84
$
```
