# Exemples de diffusion (broadcasting)

Examillons quelques exemples pour comprendre comment la diffusion (broadcasting) fonctionne dans différents scénarios.

- Exemple 1 :

```python
import numpy as np

a = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
b = np.array([1.0, 2.0, 3.0])
result = a + b
```

Dans ce cas, `b` est ajouté à chaque ligne de `a`. Le résultat est un tableau 2D ayant la même forme que `a`, où chaque élément est la somme des éléments correspondants dans `a` et `b`.

- Exemple 2 :

```python
import numpy as np

a = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
b = np.array([1.0, 2.0])
result = a + b
```

Dans ce cas, la diffusion (broadcasting) échoue car les dimensions finales de `a` et `b` ne sont pas égales. Il est impossible d'aligner les valeurs dans les lignes de `a` avec les éléments de `b` pour une addition élément par élément.
