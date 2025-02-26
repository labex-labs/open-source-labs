# Interfaces et vérification de type

Modifiez la fonction `print_table()` de sorte qu'elle vérifie si l'instance de formateur fournie hérite de `TableFormatter`. Si ce n'est pas le cas, lève une `TypeError`.

Votre nouveau code devrait détecter des situations telles que celles-ci :

```python
>>> import stock, reader, tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> class MyFormatter:
        def headings(self,headers): pass
        def row(self,rowdata): pass

>>> tableformat.print_table(portfolio, ['name','shares','price'], MyFormatter())
Traceback (most recent call last):
...
TypeError: Expected a TableFormatter
>>>
```

Ajouter une vérification de ce type peut ajouter un certain degré de sécurité au programme. Cependant, vous devriez encore être conscient que la vérification de type est assez faible en Python. Il n'est pas garanti que l'objet passé en tant que formateur fonctionnera correctement même s'il hérite de la bonne classe de base. La partie suivante aborde ce problème.
