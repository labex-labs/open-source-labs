# Exercice 5.2 : Modification des données d'instance

Essayez de définir un nouvel attribut sur l'une des instances ci-dessus :

```python
>>> goog.date = '6/11/2007'
>>> goog.__dict__
... regardez la sortie...
>>> ibm.__dict__
... regardez la sortie...
>>>
```

Dans la sortie ci-dessus, vous remarquerez que l'instance `goog` a un attribut `date` tandis que l'instance `ibm` n'en a pas. Il est important de noter que Python ne pose vraiment aucune restriction sur les attributs. Par exemple, les attributs d'une instance ne sont pas limités à ceux définis dans la méthode `__init__()`.

Au lieu de définir un attribut, essayez de placer une nouvelle valeur directement dans l'objet `__dict__` :

```python
>>> goog.__dict__['time'] = '9:45am'
>>> goog.time
'9:45am'
>>>
```

Ici, vous remarquez vraiment le fait qu'une instance n'est qu'une couche au-dessus d'un dictionnaire. Notez : il faut souligner que la manipulation directe du dictionnaire est peu courante - vous devriez toujours écrire votre code pour utiliser la syntaxe (.).
