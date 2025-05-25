# Exercício 3.15: Funções `main()`

No arquivo `report.py`, adicione uma função `main()` que aceite uma lista de opções de linha de comando e produza a mesma saída de antes. Você deve ser capaz de executá-la interativamente assim:

```python
>>> import report
>>> report.main(['/home/labex/project/report.py', '/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv'])
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

Modifique o arquivo `pcost.py` para que ele tenha uma função `main()` semelhante:

```python
>>> import pcost
>>> pcost.main(['/home/labex/project/pcost.py', '/home/labex/project/portfolio.csv'])
Total cost: 44671.15
>>>
```
