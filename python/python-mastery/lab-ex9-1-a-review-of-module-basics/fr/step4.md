# from module import

Redémarrez Python et importez un symbole sélectionné à partir d'un module.

```python
>>> ############### [ RESTART ] ###############
>>> from simplemod import foo
Chargé simplemod
>>> foo()
x est 42
>>>
```

Remarquez comment cela a chargé le module entier (observez la sortie de la fonction print et comment la variable `x` est utilisée).

Lorsque vous utilisez `from`, l'objet module lui-même n'est pas visible. Par exemple :

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name'simplemod' is not defined
>>>
```

Assurez-vous de comprendre que lorsque vous exportez des choses à partir d'un module, il s'agit simplement de références de nom. Par exemple, essayez ceci et expliquez :

```python
>>> from simplemod import x,foo
>>> x
42
>>> foo()
x est 42
>>> x = 13
>>> foo()
x est 42                   #!! Veuillez expliquer
>>> x
13
>>>
```
