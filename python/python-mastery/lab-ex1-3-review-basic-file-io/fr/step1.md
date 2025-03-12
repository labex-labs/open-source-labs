# Comprendre le problème

Dans cette étape, nous allons d'abord comprendre le problème que nous devons résoudre, puis examiner les données avec lesquelles nous allons travailler. C'est une première étape importante dans toute tâche de programmation car elle nous aide à savoir exactement ce que nous visons et quelles ressources nous avons à notre disposition.

Dans votre répertoire de projet, il y a un fichier nommé `portfolio.dat`. Ce fichier stocke des informations sur un portefeuille d'actions. Un portefeuille est comme une collection de différentes actions que possède un investisseur. Chaque ligne de ce fichier représente un achat d'action unique. Le format de chaque ligne est le suivant :

```
[Symbole de l'action] [Nombre d'actions] [Prix par action]
```

Le symbole de l'action est un code court qui représente les actions d'une entreprise particulière. Le nombre d'actions nous indique combien d'unités de cette action ont été achetées, et le prix par action est le coût d'une unité de cette action.

Regardons un exemple. Considérons la première ligne du fichier :

```
AA 100 32.20
```

Cette ligne indique que 100 actions de l'action avec le symbole "AA" ont été achetées. Chaque action a coûté 32,20 $.

Si vous voulez voir ce qui se trouve à l'intérieur du fichier `portfolio.dat`, vous pouvez exécuter la commande suivante dans le terminal. La commande `cat` est un outil utile dans le terminal qui vous permet de visualiser le contenu d'un fichier.

```bash
cat ~/project/portfolio.dat
```

Maintenant, votre tâche est de créer un programme Python nommé `pcost.py`. Ce programme effectuera trois tâches principales :

1. Tout d'abord, il doit ouvrir et lire le fichier `portfolio.dat`. Ouvrir un fichier en Python permet à notre programme d'accéder aux données stockées à l'intérieur.
2. Ensuite, il doit calculer le coût total de tous les achats d'actions dans le portefeuille. Pour ce faire, pour chaque ligne du fichier, nous devons multiplier le nombre d'actions par le prix par action. Après avoir obtenu ces valeurs pour chaque ligne, nous les additionnons toutes. Cela nous donne le montant total d'argent dépensé pour toutes les actions du portefeuille.
3. Enfin, le programme doit afficher le coût total. De cette façon, nous pouvons voir le résultat de nos calculs.

Commençons par créer le fichier `pcost.py`. Vous pouvez utiliser l'éditeur pour ouvrir et modifier ce fichier. Il a déjà été créé pour vous lors de l'étape de configuration. Ce fichier sera l'endroit où vous écrirez le code Python pour résoudre le problème que nous venons de discuter.
