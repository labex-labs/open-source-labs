# Fonction pour inverser une liste

Écrivez une fonction Python appelée `reverse(itr)` qui prend une liste ou une chaîne de caractères en argument et renvoie une nouvelle liste ou chaîne de caractères qui contient les éléments ou les caractères dans l'ordre inverse.

Votre fonction doit répondre aux exigences suivantes :

- La fonction doit s'appeler `reverse`
- La fonction doit prendre un seul argument, qui est une liste ou une chaîne de caractères
- La fonction doit renvoyer une nouvelle liste ou chaîne de caractères qui contient les éléments ou les caractères dans l'ordre inverse
- La fonction ne doit pas modifier la liste ou la chaîne d'origine

```python
def reverse(itr):
  return itr[::-1]
```

```python
reverse([1, 2, 3]) # [3, 2, 1]
reverse('snippet') # 'teppins'
```
