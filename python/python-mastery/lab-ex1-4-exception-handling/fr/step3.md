# Expérimentation interactive

Python propose un mode interactif qui vous permet d'exécuter du code immédiatement. Cela est très utile pour tester votre code et essayer de nouvelles choses. Dans cette étape, nous allons apprendre à appeler une fonction directement depuis l'interpréteur Python.

## Exécution de Python en mode interactif

Pour exécuter un script Python puis entrer en mode interactif, vous pouvez utiliser le flag `-i`. Ce flag indique à Python de rester en mode interactif après avoir exécuté le script. Voici comment faire :

```bash
cd /home/labex/project
python3 -i pcost.py
```

Découpons ce que fait cette commande :

1. Tout d'abord, `cd /home/labex/project` change le répertoire courant pour `/home/labex/project`. C'est là que se trouve notre script `pcost.py`.
2. Ensuite, `python3 -i pcost.py` exécute le script `pcost.py`. Une fois le script terminé, Python reste en mode interactif.
3. En mode interactif, vous pouvez taper des commandes Python directement dans le terminal.

Après avoir exécuté la commande, vous verrez la sortie du script `pcost.py`, suivie de l'invite Python (`>>>`). Cette invite indique que vous pouvez maintenant entrer des commandes Python.

## Appel de votre fonction de manière interactive

Une fois que vous êtes en mode interactif, vous pouvez appeler la fonction `portfolio_cost()` avec différents noms de fichiers. Cela vous permet de voir comment la fonction se comporte avec diverses entrées. Voici un exemple :

```python
>>> portfolio_cost('/home/labex/project/portfolio.dat')
44671.15
>>> portfolio_cost('/home/labex/project/portfolio2.dat')
19908.75
>>> portfolio_cost('/home/labex/project/portfolio3.dat')
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

En utilisant cette approche interactive, vous pouvez :

- Tester votre fonction avec différentes entrées pour voir si elle fonctionne comme prévu.
- Expérimenter le comportement de la fonction dans diverses conditions.
- Déboguer votre code en direct en voyant les résultats immédiats de vos appels de fonction.

## Avantages du mode interactif

Le mode interactif présente plusieurs avantages :

1. Vous pouvez tester rapidement différents scénarios sans avoir à exécuter tout le script à chaque fois.
2. Vous pouvez inspecter immédiatement les variables et les résultats des expressions, ce qui vous aide à comprendre ce qui se passe dans votre code.
3. Vous pouvez tester de petits morceaux de code sans créer un programme complet. C'est idéal pour apprendre et tester de nouvelles idées.
4. C'est une excellente façon d'apprendre et d'expérimenter avec Python car vous obtenez des retours immédiats.

## Sortie du mode interactif

Lorsque vous avez terminé vos expériences, vous pouvez quitter le mode interactif de deux manières :

- Tapez `exit()` puis appuyez sur Entrée. C'est un moyen simple de terminer la session interactive.
- Appuyez sur Ctrl+D (sur Unix/Linux). C'est un raccourci qui permet également de quitter le mode interactif.

Tout au long de votre parcours de programmation en Python, la technique de définition de fonctions et de test interactif sera extrêmement précieuse pour le développement et le débogage. Elle vous permet d'itérer rapidement sur votre code et de trouver et de corriger les problèmes.
