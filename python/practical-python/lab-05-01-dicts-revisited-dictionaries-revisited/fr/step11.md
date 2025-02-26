# Lecture des attributs avec héritage simple

Dans les hiérarchies d'héritage, les attributs sont trouvés en remontant l'arbre d'héritage dans l'ordre.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(D): pass
```

Avec l'héritage simple, il existe un seul chemin vers le sommet. Vous arrêtez au premier match.
