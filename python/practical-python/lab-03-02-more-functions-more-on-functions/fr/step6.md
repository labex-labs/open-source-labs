# Plusieurs valeurs de retour

Les fonctions ne peuvent renvoyer qu'une seule valeur. Cependant, une fonction peut renvoyer plusieurs valeurs en les renvoyant dans un tuple.

```python
def divide(a,b):
    q = a // b      # Quotient
    r = a % b       # Reste
    return q, r     # Renvoie un tuple
```

Exemple d'utilisation :

```python
x, y = divide(37,5) # x = 7, y = 2

x = divide(37, 5)   # x = (7, 2)
```
