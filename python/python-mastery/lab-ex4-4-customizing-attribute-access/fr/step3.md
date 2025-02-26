# La délégation comme alternative à l'héritage

La délégation est parfois utilisée comme alternative à l'héritage. L'idée est presque la même que pour la classe proxy que vous avez définie en partie (b). Essayez de définir la classe suivante :

```python
>>> class Spam:
        def a(self):
            print('Spam.a')
        def b(self):
            print('Spam.b')

>>>
```

Maintenant, créez une classe qui s'enveloppe autour d'elle et redéfinissez certaines des méthodes :

```python
>>> class MySpam:
        def __init__(self):
            self._spam = Spam()
        def a(self):
            print('MySpam.a')
            self._spam.a()
        def c(self):
            print('MySpam.c')
        def __getattr__(self, name):
            return getattr(self._spam, name)

>>> s = MySpam()
>>> s.a()
MySpam.a
Spam.a
>>> s.b()
Spam.b
>>> s.c()
MySpam.c
>>>
```

Remarquez attentivement que la classe résultante ressemble beaucoup à l'héritage. Par exemple, la méthode `a()` fait quelque chose de similaire à l'appel de `super()`. La méthode `b()` est récupérée via la méthode `__getattr__()` qui délègue à l'instance `Spam` maintenue à l'intérieur.

**Discussion**

La méthode `__getattr__()` est généralement définie sur les classes qui agissent comme des enveloppes autour d'autres objets. Cependant, vous devez être conscient que le processus d'enveloppement d'un autre objet de cette manière introduit souvent d'autres complexités. Par exemple, l'objet d'enveloppe peut casser la vérification de type si une autre partie de l'application utilise la fonction `isinstance()`.

La délégation de méthodes via `__getattr__()` ne fonctionne pas non plus avec les méthodes spéciales telles que `__getitem__()`, `__enter__()` et ainsi de suite. Si une classe utilise largement de telles méthodes, vous devrez fournir des fonctions similaires dans votre classe d'enveloppe.
