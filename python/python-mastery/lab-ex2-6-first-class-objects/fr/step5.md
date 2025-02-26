# Pensée profonde

Dans cet exercice, vous avez écrit deux fonctions, `read_csv_as_dicts()` et `read_csv_as_columns()`. Ces fonctions présentent les données à l'utilisateur de la même manière. Par exemple :

```python
>>> data1 = read_csv_as_dicts('ctabus.csv', [str, str, str, int])
>>> len(data1)
577563
>>> data1[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data1[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>

>>> data2 = read_csv_as_columns('ctabus.csv', [str, str, str, int])
>>> len(data2)
577563
>>> data2[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> data2[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>
```

En fait, vous pouvez utiliser l'une ou l'autre des fonctions dans le code d'analyse des données CTA que vous avez écrit. Cependant, en réalité, des choses complètement différentes se passent. La fonction `read_csv_as_columns()` stocke les données sous une représentation différente. Elle s'appuie sur les protocoles de séquence de Python (méthodes magiques) pour vous présenter les informations d'une manière plus utile.

Cela fait réellement partie d'un concept de programmation beaucoup plus large appelé "abstraction des données". Lors de la rédaction de programmes, la manière dont les données sont présentées est souvent plus importante que la manière dont les données sont effectivement combinées en arrière-plan. Bien que nous présentions les données sous forme d'une séquence de dictionnaires, il y a une grande flexibilité quant à la manière dont cela se passe effectivement en coulisse. C'est une idée puissante et quelque chose à considérer lors de la rédaction de vos propres programmes.
