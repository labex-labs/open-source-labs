# reload() défaillant

Créez une instance :

```python
>>> import simplemod
>>> s = simplemod.Spam()
>>> s.yow()
Yow!
>>>
```

Maintenant, allez dans le fichier `simplemod.py` et changez l'implémentation de `Spam.yow()` comme suit :

```python
# simplemod.py
...

class Spam:
    def yow(self):
        print('Plus de Yow!')
```

Maintenant, observez ce qui se passe lors d'un rechargement. Ne redémarrez pas Python pour cette partie.

```python
>>> importlib.reload(simplemod)
Chargé simplemod
<module'simplemod' from'simplemod.py'>
>>> s.yow()
'Yow!'
>>> t = simplemod.Spam()
>>> t.yow()
'Plus de Yow!'
>>>
```

Remarquez comment vous avez deux instances de `Spam`, mais qu'elles utilisent des implémentations différentes de la méthode `yow()`. Oui, en fait les deux versions du code sont chargées en même temps. Vous trouverez également d'autres bizarreries. Par exemple :

```python
>>> s
<simplemod.Spam objet à 0x1006940b8>
>>> isinstance(s, simplemod.Spam)
Faux
>>> isinstance(t, simplemod.Spam)
Vrai
>>>
```

En résumé : Il est probablement préférable de ne pas compter sur le rechargement pour quoi que ce soit d'important. Cela peut être acceptable si vous essayez simplement de déboguer certaines choses (pourvu que vous soyez conscient de ses limites et de ses dangers).
