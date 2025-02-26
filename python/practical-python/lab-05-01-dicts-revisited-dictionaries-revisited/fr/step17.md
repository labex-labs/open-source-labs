# Certaines précautions

L'héritage multiple est un outil puissant. Rappelez-vous que avec le pouvoir vient la responsabilité. Certains frameworks / bibliothèques l'utilisent parfois pour des fonctionnalités avancées impliquant la composition de composants. Maintenant, oubliez que vous avez lu ça.

Dans la Section 4, vous avez défini une classe `Stock` qui représentait une position en actions. Dans cet exercice, nous allons utiliser cette classe. Redémarrez l'interpréteur et créez quelques instances :

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> goog = Stock('GOOG',100,490.10)
>>> ibm  = Stock('IBM',50, 91.23)
>>>
```
