# Création d'objets Stock

Maintenant que nous avons défini notre classe `Stock`, il est temps de la mettre en pratique. Créer des instances d'une classe revient à créer des exemples spécifiques à partir d'un modèle général. Dans ce cas, la classe `Stock` est notre modèle, et nous allons créer quelques objets d'actions. Après avoir créé ces objets, nous apprendrons à accéder à leurs attributs (caractéristiques) et à leurs méthodes (actions qu'ils peuvent effectuer).

1. Tout d'abord, nous devons ouvrir un terminal dans le WebIDE. Le terminal est comme un centre de commandes où nous pouvons donner des instructions à notre ordinateur. Pour l'ouvrir, cliquez sur "Terminal" dans le menu.

2. Une fois le terminal ouvert, nous devons nous assurer que nous sommes dans le bon répertoire de projet. Le répertoire de projet est l'endroit où tous les fichiers pertinents de notre projet sont stockés. Si vous n'êtes pas déjà dans le répertoire de projet, utilisez la commande suivante pour y accéder :

```bash
cd /home/labex/project
```

3. Maintenant, nous voulons démarrer Python en mode interactif avec notre fichier `stock.py`. Le mode interactif nous permet de tester notre code étape par étape et de voir immédiatement les résultats. Le fichier `stock.py` contient la définition de notre classe `Stock`. Utilisez la commande suivante :

```bash
python3 -i stock.py
```

Le drapeau `-i` est important ici. Il indique à Python d'exécuter d'abord le script `stock.py`. Après avoir exécuté le script, il démarre une session interactive. Dans cette session, nous pouvons accéder à toutes les classes et variables définies dans le script `stock.py`.

4. Créons un nouvel objet `Stock` pour les actions de Google. Créer un objet revient à créer une instance spécifique de la classe `Stock` avec des valeurs particulières. Utilisez le code suivant :

```python
s = Stock('GOOG', 100, 490.10)
```

Cette ligne de code crée une nouvelle instance de la classe `Stock`. Voici ce que chaque valeur signifie :

- Nom : 'GOOG' - C'est le symbole des actions de Google.
- Parts : 100 - Cela représente le nombre de parts d'actions de Google que nous possédons.
- Prix : 490.10 - C'est le prix par part des actions de Google.

5. Maintenant que nous avons notre objet `Stock`, nous pouvons accéder à ses attributs. Les attributs sont comme les propriétés d'un objet. Pour accéder à un attribut, nous utilisons le nom de l'objet suivi d'un point et du nom de l'attribut.

```python
s.name
```

Lorsque vous exécutez ce code, il affichera le nom de l'action :

```
'GOOG'
```

Accédons au nombre de parts :

```python
s.shares
```

La sortie sera le nombre de parts que nous avons défini :

```
100
```

Enfin, accédons au prix par part :

```python
s.price
```

La sortie sera le prix par part :

```
490.1
```

6. Notre classe `Stock` a une méthode appelée `cost()`. Une méthode est comme une action qu'un objet peut effectuer. Dans ce cas, la méthode `cost()` calcule le coût total de nos parts. Pour appeler cette méthode, utilisez le code suivant :

```python
s.cost()
```

La sortie sera le coût total :

```
49010.0
```

La méthode `cost()` fonctionne en multipliant le nombre de parts (100) par le prix par part (490.10), ce qui nous donne 49010.0.
