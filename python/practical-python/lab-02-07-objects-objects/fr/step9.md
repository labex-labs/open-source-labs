# Vérification de type

Comment déterminer si un objet est d'un type spécifique.

```python
if isinstance(a, list):
    print('a est une liste')
```

Vérification pour l'un de plusieurs types possibles.

```python
if isinstance(a, (list,tuple)):
    print('a est une liste ou un tuple')
```

\*Attention : Ne poussez pas trop loin la vérification de type. Cela peut entraîner une complexité excessive du code. En général, vous ne le feriez que si cela permet de prévenir les erreurs courantes commises par d'autres utilisant votre code.
