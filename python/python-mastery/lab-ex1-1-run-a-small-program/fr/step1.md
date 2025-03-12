# Vérifier l'installation de Python et utiliser l'interpréteur interactif

L'interpréteur interactif Python est un outil très utile. Il vous permet d'exécuter du code Python ligne par ligne et de voir immédiatement les résultats. C'est idéal pour les débutants car vous pouvez tester de petits morceaux de code sans avoir à écrire un programme complet. Avant de commencer à écrire des programmes complets, nous devons nous assurer que Python est correctement installé sur votre système. Ensuite, nous apprendrons à utiliser cet interpréteur pour exécuter du code Python.

## Lancer l'interpréteur Python

1. Tout d'abord, nous devons ouvrir un terminal dans le WebIDE. Le terminal est comme un centre de commandes où vous pouvez taper des commandes pour interagir avec votre ordinateur. Vous trouverez un onglet de terminal en bas de l'écran. Une fois que vous l'avez ouvert, vous êtes prêt à commencer à taper des commandes.

2. Dans le terminal, nous allons vérifier si Python est installé et quelle version vous avez. Tapez la commande suivante puis appuyez sur Entrée :

   ```bash
   python3 --version
   ```

   Cette commande demande à votre système d'afficher la version de Python actuellement installée. Si Python est correctement installé, vous verrez une sortie similaire à :

   ```
   Python 3.10.x
   ```

   Le `x` ici représente un numéro de correctif spécifique, qui peut varier en fonction de votre installation.

3. Maintenant que nous savons que Python est installé, lançons l'interpréteur interactif Python. Tapez la commande suivante dans le terminal et appuyez sur Entrée :

   ```bash
   python3
   ```

   Après avoir appuyé sur Entrée, vous verrez des informations sur la version de Python et d'autres détails. La sortie ressemblera à ceci :

   ```
   Python 3.10.x (default, ...)
   [GCC x.x.x] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   ```

   L'invite `>>>` est un signal indiquant que l'interpréteur Python est lancé et en attente que vous entriez des commandes Python.

## Essayer des commandes Python simples

Maintenant que l'interpréteur Python est en cours d'exécution, essayons quelques commandes Python de base. Ces commandes vous aideront à comprendre le fonctionnement de Python et à utiliser l'interpréteur.

1. À l'invite `>>>` , tapez la commande suivante et appuyez sur Entrée :

   ```python
   >>> print('Hello World')
   ```

   La fonction `print` en Python est utilisée pour afficher du texte à l'écran. Lorsque vous exécutez cette commande, vous verrez la sortie suivante :

   ```
   Hello World
   >>>
   ```

   Cela montre que la fonction `print` a réussi à afficher le texte 'Hello World'.

2. Essayons un simple calcul mathématique. À l'invite, tapez :

   ```python
   >>> 2 + 3
   ```

   Python évaluera automatiquement cette expression et vous montrera le résultat. Vous verrez :

   ```
   5
   >>>
   ```

   Cela démontre que Python peut effectuer des opérations arithmétiques de base.

3. Ensuite, nous allons créer une variable et l'utiliser. Les variables en Python sont utilisées pour stocker des données. Tapez les commandes suivantes à l'invite :

   ```python
   >>> message = "Learning Python"
   >>> print(message)
   ```

   Dans la première ligne, nous créons une variable nommée `message` et nous y stockons la chaîne de caractères "Learning Python". Dans la deuxième ligne, nous utilisons la fonction `print` pour afficher la valeur stockée dans la variable `message`. La sortie sera :

   ```
   Learning Python
   >>>
   ```

   L'interpréteur Python exécute chaque ligne de code dès que vous l'avez entrée. Cela en fait un excellent outil pour tester rapidement des idées et apprendre les concepts de Python.

## Quitter l'interpréteur

Lorsque vous avez terminé d'expérimenter avec l'interpréteur Python, vous pouvez le quitter en utilisant l'une des méthodes suivantes :

1. Vous pouvez taper la commande suivante à l'invite `>>>` et appuyer sur Entrée :

   ```python
   >>> exit()
   ```

   Ou vous pouvez utiliser cette commande alternative :

   ```python
   >>> quit()
   ```

   Ces deux commandes indiquent à l'interpréteur Python de s'arrêter et de vous renvoyer au terminal normal.

2. Une autre façon de quitter est en appuyant sur Ctrl+D sur votre clavier. C'est un raccourci qui arrête également l'interpréteur Python.

Après avoir quitté l'interpréteur, vous reviendrez à l'invite de terminal normale, où vous pouvez exécuter d'autres commandes sur votre système.
