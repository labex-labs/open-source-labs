# Rendre les choses sensées

L'utilisation de mixins peut être un outil utile pour les concepteurs de frameworks pour réduire la quantité de code à écrire. Cependant, forcer les utilisateurs à se souvenir de la manière de composer correctement les classes et d'utiliser l'héritage multiple peut les rendre dingues. Dans l'exercice 3.5, vous avez écrit une fonction `create_formatter()` qui a facilité la création d'un formatteur personnalisé. Prenez cette fonction et étendez-la pour qu'elle comprenne quelques arguments optionnels liés aux classes mixin. Par exemple :

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('csv', column_formats=['"%s"','%d','%0.2f'])
>>> print_table(portfolio, ['name','shares','price'], formatter)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44

>>> formatter = create_formatter('text', upper_headers=True)
>>> print_table(portfolio, ['name','shares','price'], formatter)
      NAME     SHARES      PRICE
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

En coulisse, la fonction `create_formatter()` composera correctement les classes et renverra une instance correcte de `TableFormatter`.
