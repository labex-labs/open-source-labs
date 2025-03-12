# Comprendre les générateurs Python

Commençons par revoir ce que sont les générateurs en Python. En Python, les générateurs sont un type spécial de fonction. Ils sont différents des fonctions ordinaires. Lorsque vous appelez une fonction ordinaire, elle s'exécute du début à la fin et retourne une seule valeur. Cependant, une fonction générateur retourne un itérateur, qui est un objet à travers lequel nous pouvons itérer, ce qui signifie que nous pouvons accéder à ses valeurs une par une.

Les générateurs utilisent l'instruction `yield` pour retourner des valeurs. Au lieu de retourner toutes les valeurs d'un coup comme une fonction ordinaire, un générateur retourne les valeurs une à une. Après avoir rendu une valeur, le générateur suspend son exécution. La prochaine fois que nous demandons une valeur, il reprend l'exécution là où il s'était arrêté.

## Créer un générateur simple

Maintenant, créons un générateur simple. Dans l'IDE Web, vous devez créer un nouveau fichier. Ce fichier contiendra le code de notre générateur. Nommez le fichier `generator_demo.py` et placez - le dans le répertoire `/home/labex/project`. Voici le contenu que vous devriez mettre dans le fichier :

```python
# Generator function that counts down from n
def countdown(n):
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Countdown complete!")

# Create a generator object
counter = countdown(5)

# Drive the generator manually
print(next(counter))  # 5
print(next(counter))  # 4
print(next(counter))  # 3

# Iterate through remaining values
for value in counter:
    print(value)  # 2, 1
```

Dans ce code, nous définissons d'abord une fonction générateur appelée `countdown`. Cette fonction prend un nombre `n` comme argument et compte à rebours de `n` à 1. À l'intérieur de la fonction, nous utilisons une boucle `while` pour décrémenter `n` et rendre chaque valeur. Lorsque nous appelons `countdown(5)`, cela crée un objet générateur nommé `counter`.

Nous utilisons ensuite la fonction `next()` pour obtenir manuellement des valeurs du générateur. Chaque fois que nous appelons `next(counter)`, le générateur reprend l'exécution là où il s'était arrêté et rend la valeur suivante. Après avoir obtenu manuellement trois valeurs, nous utilisons une boucle `for` pour itérer à travers les valeurs restantes dans le générateur.

Pour exécuter ce code, ouvrez le terminal et exécutez la commande suivante :

```bash
python3 /home/labex/project/generator_demo.py
```

Lorsque vous exécutez le code, vous devriez voir la sortie suivante :

```
Starting countdown from 5
5
4
3
2
1
Countdown complete!
```

Remarquons le comportement de la fonction générateur :

1. La fonction générateur commence son exécution lorsque nous appelons `next(counter)` pour la première fois. Avant cela, la fonction est simplement définie et aucun décompte réel n'a commencé.
2. Elle se met en pause à chaque instruction `yield`. Après avoir rendu une valeur, elle s'arrête et attend le prochain appel à `next()`.
3. Lorsque nous appelons `next()` à nouveau, elle continue là où elle s'était arrêtée. Par exemple, après avoir rendu 5, elle se souvient de l'état et continue de décrémenter `n` et de rendre la valeur suivante.
4. La fonction générateur termine son exécution après que la dernière valeur a été rendue. Dans notre cas, après avoir rendu 1, elle affiche "Countdown complete!".

Cette capacité à mettre en pause et reprendre l'exécution est ce qui rend les générateurs puissants. Elle est très utile pour des tâches telles que la planification de tâches (task scheduling) et la programmation asynchrone, où nous devons effectuer plusieurs tâches de manière efficace sans bloquer l'exécution des autres tâches.
