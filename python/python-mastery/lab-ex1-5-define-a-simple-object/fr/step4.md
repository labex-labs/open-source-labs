# Travailler avec plusieurs objets Stock

En programmation orientée objet, une classe est comme un modèle, et les instances de cette classe sont les objets réels créés à partir de ce modèle. Notre classe `Stock` est un modèle pour représenter les actions. Nous pouvons créer plusieurs instances de cette classe `Stock` pour représenter différentes actions. Chaque instance aura son propre ensemble d'attributs, tels que le nom de l'action, le nombre de parts et le prix par part.

1. Avec la session interactive Python toujours en cours d'exécution, nous allons créer un autre objet `Stock`. Cette fois, il représentera IBM. Pour créer une instance de la classe `Stock`, nous appelons le nom de la classe comme si c'était une fonction et nous passons les arguments nécessaires. Les arguments ici sont le nom de l'action, le nombre de parts et le prix par part.

```python
t = Stock('IBM', 50, 91.5)
```

Dans cette ligne de code, nous créons un nouvel objet `Stock` nommé `t` qui représente IBM. Il a 50 parts, et chaque part coûte 91,5 $.

2. Maintenant, nous voulons calculer le coût de cette nouvelle action. La classe `Stock` a une méthode nommée `cost()` qui calcule le coût total de l'action en multipliant le nombre de parts par le prix par part.

```python
t.cost()
```

Lorsque vous exécutez ce code, Python appellera la méthode `cost()` sur l'objet `t` et renverra le coût total.

Sortie :

```
4575.0
```

3. Nous pouvons formater et afficher nos informations sur les actions d'une manière agréable et organisée en utilisant le formatage de chaînes de caractères de Python. Le formatage de chaînes de caractères nous permet de spécifier comment différents types de données doivent être présentés dans une chaîne.

```python
print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
```

Dans ce code, nous utilisons le formatage de chaînes de caractères de l'ancien style en Python. L'opérateur `%` est utilisé pour substituer des valeurs dans un modèle de chaîne. Le modèle de chaîne `'%10s %10d %10.2f'` définit comment le nom de l'action, le nombre de parts et le prix doivent être formatés.

Sortie :

```
      GOOG        100     490.10
```

Cette chaîne formatée fonctionne comme suit :

- `%10s` formate une chaîne dans un champ de 10 caractères de large (aligné à droite). Cela signifie que le nom de l'action sera placé dans un espace de 10 caractères de large et sera aligné à droite dans cet espace.
- `%10d` formate un entier dans un champ de 10 caractères de large. Ainsi, le nombre de parts sera placé dans un espace de 10 caractères de large.
- `%10.2f` formate un nombre à virgule flottante avec 2 décimales dans un champ de 10 caractères de large. Le prix sera affiché avec deux décimales et placé dans un espace de 10 caractères de large.

4. Maintenant, formattons les informations sur les actions IBM de la même manière. Nous devons simplement remplacer le nom de l'objet de `s` à `t` dans le code de formatage de chaîne.

```python
print('%10s %10d %10.2f' % (t.name, t.shares, t.price))
```

Sortie :

```
       IBM         50      91.50
```

5. En Python moderne, nous pouvons également utiliser les f - chaînes pour le formatage. Les f - chaînes sont plus lisibles et plus faciles à utiliser. Comparons les coûts des deux actions à l'aide de f - chaînes.

```python
print(f"Google stock costs ${s.cost()}, IBM stock costs ${t.cost()}")
```

Dans cette f - chaîne, nous intégrons directement des expressions à l'intérieur d'accolades `{}`. Python évaluera ces expressions et insérera les résultats dans la chaîne.

Sortie :

```
Google stock costs $49010.0, IBM stock costs $4575.0
```

6. Lorsque vous avez terminé vos expériences, il est temps de quitter le mode interactif Python. Vous pouvez le faire en utilisant la fonction `exit()`.

```python
exit()
```

Chaque objet Stock conserve son propre ensemble d'attributs, ce qui démontre comment les instances de classe fonctionnent en programmation orientée objet. Cela nous permet de créer plusieurs objets d'actions, chacun avec des valeurs différentes, tout en partageant les mêmes méthodes.
