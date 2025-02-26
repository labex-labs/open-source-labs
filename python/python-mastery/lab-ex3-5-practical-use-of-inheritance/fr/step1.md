# Préparation

Un usage majeur des classes en Python est d'écrire du code qui peut être étendu/ adapté de diverses manières. Pour illustrer, dans l'exercice 3.2, vous avez créé une fonction `print_table()` qui permettait de générer des tableaux. Vous l'avez utilisée pour générer la sortie à partir de la liste `portfolio`. Par exemple :

```python
>>> import stock
>>> import reader
>>> import tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> tableformat.print_table(portfolio, ['name','shares','price'])
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

Supposons que vous vouliez que la fonction `print_table()` soit capable de générer des tableaux dans un nombre quelconque de formats de sortie tels que CSV, XML, HTML, Excel, etc. Essayez de modifier la fonction pour prendre en charge tous ces formats de sortie d'un coup serait pénible. Une meilleure façon de faire cela consiste à déplacer le code de formatage lié à la sortie dans une classe et à utiliser l'héritage pour implémenter différents formats de sortie.
