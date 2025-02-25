# Composer des fonctions

## Problème

Écrire une fonction appelée `compose(*fns)` qui accepte une ou plusieurs fonctions en arguments et renvoie une nouvelle fonction qui est le résultat de la composition des fonctions d'entrée de droite à gauche. La dernière (la plus à droite) fonction peut accepter un ou plusieurs arguments ; les fonctions restantes doivent être unaire.

## Exemple

```python
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```

Dans l'exemple ci-dessus, nous définissons deux fonctions `add5` et `multiply`. Nous utilisons ensuite la fonction `compose()` pour créer une nouvelle fonction appelée `multiply_and_add_5` qui multiplie d'abord ses deux arguments puis ajoute 5 au résultat. Lorsque nous appelons `multiply_and_add_5(5, 2)`, nous obtenons le résultat `15`.
