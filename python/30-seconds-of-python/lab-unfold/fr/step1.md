# Détacher une liste

Votre tâche consiste à implémenter la fonction `unfold` qui prend une fonction itératrice et une valeur de graine initiale en arguments. La fonction itératrice accepte un seul argument (`seed`) et doit toujours renvoyer une liste avec deux éléments ([`valeur`, `prochaine graine`]) ou `False` pour terminer. La fonction `unfold` devrait utiliser une fonction génératrice, `fn_generator`, qui utilise une boucle `while` pour appeler la fonction itératrice et `produire` la `valeur` jusqu'à ce qu'elle renvoie `False`. Enfin, la fonction `unfold` devrait utiliser une compréhension de liste pour renvoyer la liste qui est produite par le générateur, en utilisant la fonction itératrice.

Implémentez la fonction `unfold` :

```python
def unfold(fn, seed):
    # votre code ici
```

### Entrée

- Une fonction itératrice `fn` qui accepte un seul argument (`seed`) et doit toujours renvoyer une liste avec deux éléments ([`valeur`, `prochaine graine`]) ou `False` pour terminer.
- Une valeur de graine initiale `seed`.

### Sortie

- Une liste qui est produite par le générateur, en utilisant la fonction itératrice.

```python
def unfold(fn, seed):
  def fn_generator(val):
    while True:
      val = fn(val[1])
      if val == False: break
      yield val[0]
  return [i for i in fn_generator([None, seed])]
```

```python
f = lambda n: False if n > 50 else [-n, n + 10]
unfold(f, 10) # [-10, -20, -30, -40, -50]
```
