# Créer un programme Python plus avancé

Maintenant que vous avez maîtrisé les bases de Python, il est temps de passer à l'étape suivante et de créer un programme Python plus avancé. Ce programme générera des motifs d'art ASCII, qui sont des designs simples mais visuellement intéressants composés de caractères textuels. En travaillant sur ce programme, vous apprendrez et appliquerez plusieurs concepts importants de Python, tels que l'importation de modules, la définition de fonctions et la gestion des arguments de ligne de commande.

## Créer le programme d'art ASCII

1. Tout d'abord, nous devons ouvrir le fichier `art.py` dans le WebIDE. Ce fichier a été créé lors du processus de configuration. Vous le trouverez dans le répertoire `/home/labex/project`. Ouvrir ce fichier est le point de départ pour écrire notre programme d'art ASCII.

2. Une fois le fichier ouvert, vous remarquerez qu'il peut contenir du contenu existant. Nous devons le supprimer car nous allons écrire notre propre code à partir de zéro. Supprimez donc tout le contenu existant dans le fichier. Ensuite, copiez le code suivant dans le fichier `art.py`. Ce code est le cœur de notre générateur d'art ASCII.

   ```python
   # art.py - A program to generate ASCII art patterns

   import sys
   import random

   # Characters used for the art pattern
   chars = '\|/'

   def draw(rows, columns):
       """
       Generate and print an ASCII art pattern with the specified dimensions.

       Args:
           rows: Number of rows in the pattern
           columns: Number of columns in the pattern
       """
       for r in range(rows):
           # For each row, create a string of random characters
           line = ''.join(random.choice(chars) for _ in range(columns))
           print(line)

   # This code only runs when the script is executed directly
   if __name__ == '__main__':
       # Check if the correct number of arguments was provided
       if len(sys.argv) != 3:
           print("Error: Incorrect number of arguments")
           print("Usage: python3 art.py rows columns")
           print("Example: python3 art.py 10 20")
           sys.exit(1)

       try:
           # Convert the arguments to integers
           rows = int(sys.argv[1])
           columns = int(sys.argv[2])

           # Call the draw function with the specified dimensions
           draw(rows, columns)
       except ValueError:
           print("Error: Both arguments must be integers")
           sys.exit(1)
   ```

3. Après avoir copié le code dans le fichier, il est important de sauvegarder votre travail. Vous pouvez le faire en appuyant sur Ctrl + S sur votre clavier. Alternativement, vous pouvez aller dans le menu et sélectionner Fichier > Enregistrer. Sauvegarder le fichier garantit que votre code est stocké et prêt à être exécuté.

## Comprendre le code

Regardons de plus près ce que fait ce programme. Comprendre le code est crucial pour que vous puissiez le modifier et l'étendre à l'avenir.

- **Instructions d'importation** : Les lignes `import sys` et `import random` sont utilisées pour importer les modules intégrés de Python. Le module `sys` donne accès à certaines variables utilisées ou maintenues par l'interpréteur Python et à des fonctions qui interagissent fortement avec l'interpréteur. Le module `random` nous permet de générer des nombres aléatoires, que nous utiliserons pour créer des motifs d'art ASCII aléatoires.
- **Ensemble de caractères** : La ligne `chars = '\|/'` définit l'ensemble de caractères qui sera utilisé pour créer notre art ASCII. Ces caractères seront sélectionnés aléatoirement pour former les motifs.
- **La fonction `draw()`** : Cette fonction est responsable de la création des motifs d'art ASCII. Elle prend deux arguments, `rows` et `columns`, qui spécifient les dimensions du motif. À l'intérieur de la fonction, elle utilise une boucle pour créer chaque ligne du motif en sélectionnant aléatoirement des caractères de l'ensemble `chars`.
- **Bloc principal** : Le bloc `if __name__ == '__main__':` est une construction spéciale en Python. Il garantit que le code à l'intérieur de ce bloc ne s'exécute que lorsque le fichier `art.py` est exécuté directement. Si le fichier est importé dans un autre fichier Python, ce code ne s'exécutera pas.
- **Gestion des arguments** : La variable `sys.argv` contient les arguments de ligne de commande passés au programme. Nous vérifions si exactement 3 arguments sont fournis (le nom du script lui - même plus deux nombres représentant le nombre de lignes et de colonnes). Cela nous aide à nous assurer que l'utilisateur fournit les entrées correctes.
- **Gestion des erreurs** : Le bloc `try/except` est utilisé pour capturer les erreurs qui pourraient survenir. Si l'utilisateur fournit des entrées invalides, telles que des valeurs non entières pour les lignes et les colonnes, le bloc `try` lèvera une `ValueError`, et le bloc `except` affichera un message d'erreur et quittera le programme.

## Exécuter le programme

1. Pour exécuter notre programme, nous devons d'abord ouvrir un terminal dans le WebIDE. C'est dans le terminal que nous entrerons les commandes pour exécuter notre script Python.

2. Une fois le terminal ouvert, nous devons naviguer jusqu'au répertoire du projet. C'est là que se trouve notre fichier `art.py`. Utilisez la commande suivante dans le terminal :

   ```bash
   cd ~/project
   ```

   Cette commande change le répertoire de travail actuel pour le répertoire du projet.

3. Maintenant que nous sommes dans le bon répertoire, nous pouvons exécuter le programme. Utilisez la commande suivante :

   ```bash
   python3 art.py 5 10
   ```

   Cette commande demande à Python d'exécuter le script `art.py` avec 5 lignes et 10 colonnes. Lorsque vous exécutez cette commande, vous verrez un motif de caractères de 5×10 imprimé dans le terminal. La sortie ressemblera à ceci :

   ```
   |\//\\|\//
   /\\|\|//\\
   \\\/\|/|/\
   //|\\\||\|
   \|//|/\|/\
   ```

   N'oubliez pas que le motif réel est aléatoire, donc votre sortie sera différente de l'exemple montré ici.

4. Vous pouvez expérimenter avec différentes dimensions en changeant les arguments de la commande. Par exemple, essayez la commande suivante :

   ```bash
   python3 art.py 8 15
   ```

   Cela générera un motif plus grand avec 8 lignes et 15 colonnes.

5. Pour voir la gestion des erreurs en action, essayez de fournir des arguments invalides. Exécutez la commande suivante :

   ```bash
   python3 art.py
   ```

   Vous devriez voir un message d'erreur comme celui - ci :

   ```
   Error: Incorrect number of arguments
   Usage: python3 art.py rows columns
   Example: python3 art.py 10 20
   ```

## Expérimenter avec le code

Vous pouvez rendre les motifs d'art ASCII plus intéressants en modifiant l'ensemble de caractères. Voici comment vous pouvez le faire :

1. Ouvrez à nouveau le fichier `art.py` dans l'éditeur. C'est là que nous allons apporter des modifications au code.

2. Trouvez la variable `chars` dans le code. Changez - la pour utiliser différents caractères. Par exemple, vous pouvez utiliser le code suivant :

   ```python
   chars = '*#@+.'
   ```

   Cela changera l'ensemble de caractères utilisé pour créer l'art ASCII.

3. Après avoir apporté la modification, sauvegardez le fichier à nouveau en utilisant Ctrl + S ou Fichier > Enregistrer. Ensuite, exécutez le programme avec la commande suivante :

   ```bash
   python3 art.py 5 10
   ```

   Maintenant, vous verrez un motif différent utilisant vos nouveaux caractères.

Cet exercice démontre plusieurs concepts importants de Python, notamment :

- Importation de modules : Comment importer des fonctionnalités supplémentaires à partir des modules intégrés de Python.
- Définition de fonctions : Comment définir et utiliser des fonctions pour organiser votre code.
- Gestion des arguments de ligne de commande : Comment accepter et traiter les entrées utilisateur depuis la ligne de commande.
- Gestion des erreurs avec try/except : Comment gérer les erreurs de manière élégante dans votre programme.
- Manipulation de chaînes de caractères : Comment créer et manipuler des chaînes de caractères pour former les motifs d'art ASCII.
- Génération de nombres aléatoires : Comment générer des valeurs aléatoires pour créer des motifs uniques.
- Compréhensions de liste : Une façon concise de créer des listes en Python, qui est utilisée dans la fonction `draw()`.
