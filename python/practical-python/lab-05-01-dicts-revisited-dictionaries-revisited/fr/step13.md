# MRO dans l'héritage multiple

Avec l'héritage multiple, il n'y a pas de chemin unique vers le sommet. Jetons un coup d'œil à un exemple.

```python
class A: pass
class B: pass
class C(A, B): pass
class D(B): pass
class E(C, D): pass
```

Qu'est-ce qui se passe lorsque vous accédez à un attribut?

```python
e = E()
e.attr
```

Un processus de recherche d'attribut est effectué, mais quel est l'ordre? C'est un problème.

Python utilise l'**héritage multiple coopératif** qui obéit à certaines règles concernant l'ordre des classes.

- Les classes filles sont toujours vérifiées avant les classes parentes
- Les classes parentes (si multiples) sont toujours vérifiées dans l'ordre indiqué.

L'ordre de résolution des méthodes (MRO) est calculé en triant toutes les classes d'une hiérarchie selon ces règles.

```python
>>> E.__mro__
(
  <class 'E'>,
  <class 'C'>,
  <class 'A'>,
  <class 'D'>,
  <class 'B'>,
  <class 'object'>)
>>>
```

L'algorithme de base est appelé "Algorithme de linéarisation C3". Les détails précis ne sont pas importants tant que vous vous souvenez qu'une hiérarchie de classes obéit aux mêmes règles d'ordre que vous pourriez suivre si votre maison était en feu et que vous deviez évacuer - les enfants d'abord, suivis des parents.
