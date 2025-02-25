# Plus long élément

## Problème

Écrivez une fonction `longest_item(*args)` qui prend un nombre quelconque d'objets itérables ou d'objets possédant une propriété `length` et renvoie celui qui est le plus long. La fonction doit :

- Utiliser `max()` avec `len()` comme `clé` pour renvoyer l'élément ayant la plus grande longueur.
- Si plusieurs éléments ont la même longueur, le premier sera renvoyé.

## Exemple

```python
longest_item('this', 'is', 'a', 'testcase') # 'testcase'
longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]) # [1, 2, 3, 4, 5]
longest_item([1, 2, 3], 'foobar') # 'foobar'
```
