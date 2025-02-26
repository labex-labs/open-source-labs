# Module `itertools`

Le module `itertools` est un module de bibliothèque avec diverses fonctions conçues pour aider avec les itérateurs/générateurs.

```python
itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1,... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1,..., sN)
```

Toutes les fonctions traitent les données de manière itérative. Elles implémentent divers types de modèles d'itération.

Plus d'informations dans le tutoriel [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/) de PyCon '08.

Dans les exercices précédents, vous avez écrit du code qui suivait les lignes écrites dans un fichier de journal et les a analysées en une séquence de lignes. Cet exercice continue sur cette base. Assurez-vous que `stocksim.py` est toujours en cours d'exécution.
