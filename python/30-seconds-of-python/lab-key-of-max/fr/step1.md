# Création de la fonction de base

Commençons par créer le noyau de notre fonction. Nous allons la construire étape par étape. Tout d'abord, créez un fichier nommé `key_of_max.py`. Vous pouvez utiliser l'éditeur de code intégré de LabEx ou un éditeur basé sur le terminal comme `nano` ou `vim`. À l'intérieur de `key_of_max.py`, ajoutez le code suivant :

![Code editor with key_of_max function](../assets/20250214-14-44-53-838b9T58.png)

```python
def key_of_max(d):
  """
  Renvoie la clé associée à la valeur maximale dans le dictionnaire 'd'.

  Si plusieurs clés partagent la valeur maximale, l'une d'entre elles peut être renvoyée.
  """
  return max(d, key=d.get)
```

Voici une analyse détaillée :

- **`def key_of_max(d):`** : Cela définit une fonction nommée `key_of_max`. Elle prend un argument, `d`, qui représente le dictionnaire avec lequel nous allons travailler.
- **`return max(d, key=d.get)`** : C'est le cœur de la fonction. Analysons-le morceau par morceau :
  - **`max(d,...)`** : La fonction intégrée `max()` trouve l'élément le plus grand. Par défaut, si vous donnez un dictionnaire à `max()`, elle trouvera la plus grande _clé_ (par ordre alphabétique). Nous ne voulons pas cela ; nous voulons la clé _associée à_ la plus grande _valeur_.
  - **`key=d.get`** : C'est la partie cruciale. L'argument `key` indique à `max()` comment comparer les éléments. `d.get` est une méthode des dictionnaires. Lorsque vous appelez `d.get(some_key)`, elle renvoie la _valeur_ associée à `some_key`. En définissant `key=d.get`, nous disons à `max()` : "Comparez les éléments du dictionnaire `d` en utilisant leurs _valeurs_, pas leurs clés." La fonction `max()` renvoie alors la _clé_ correspondant à cette valeur maximale.
