# Créer un simple programme Python

Maintenant que nous avons confirmé que Python fonctionne correctement, il est temps de créer notre premier fichier de programme Python. Pour les débutants, c'est toujours une bonne idée de commencer par quelque chose de simple avant de passer à des programmes plus complexes. De cette façon, vous pouvez progressivement comprendre les concepts de base et la syntaxe de Python.

## Créer votre premier fichier Python

Tout d'abord, nous allons créer un nouveau fichier Python. Voici comment vous pouvez le faire :

1. Dans le WebIDE, vous remarquerez un panneau à gauche de l'écran appelé le panneau Explorateur. Ce panneau vous aide à naviguer parmi les différents fichiers et répertoires de votre projet. Localisez ce panneau.

2. Une fois que vous avez trouvé le panneau Explorateur, vous devez naviguer jusqu'au répertoire `/home/labex/project`. C'est là que nous allons stocker notre programme Python.

3. Cliquez avec le bouton droit n'importe où dans le panneau Explorateur. Un menu apparaîtra. Dans ce menu, sélectionnez "Nouveau fichier". Cette action créera un nouveau fichier vide.

4. Après avoir créé le nouveau fichier, vous devez lui donner un nom. Nommez le fichier `hello.py`. En Python, les fichiers ont généralement l'extension `.py`, qui indique qu'ils contiennent du code Python.

5. Maintenant, ouvrez le fichier `hello.py` nouvellement créé dans l'éditeur. Dans l'éditeur, tapez le code suivant :

   ```python
   # This is a simple Python program

   name = input("Enter your name: ")
   print(f"Hello, {name}! Welcome to Python programming.")
   ```

   Analysons ce code. La ligne commençant par `#` est un commentaire. Les commentaires sont utilisés pour expliquer ce que le code fait et sont ignorés par l'interpréteur Python. La fonction `input()` est utilisée pour obtenir des entrées de l'utilisateur. Elle affiche le message "Enter your name: " et attend que l'utilisateur tape quelque chose. La valeur saisie par l'utilisateur est ensuite stockée dans la variable `name`. La fonction `print()` est utilisée pour afficher une sortie à l'écran. Le `f"Hello, {name}!"` est une f-string, qui est un moyen pratique de formater des chaînes de caractères en Python. Elle vous permet d'insérer directement la valeur d'une variable dans une chaîne de caractères.

6. Après avoir tapé le code, vous devez enregistrer le fichier. Vous pouvez le faire en appuyant sur Ctrl+S sur votre clavier ou en sélectionnant Fichier > Enregistrer dans le menu. Enregistrer le fichier garantit que vos modifications sont conservées.

## Exécuter votre premier programme Python

Maintenant que vous avez créé et enregistré votre programme Python, il est temps de l'exécuter. Voici comment :

1. Ouvrez un terminal dans le WebIDE s'il n'est pas déjà ouvert. Le terminal vous permet d'exécuter des commandes et de lancer des programmes.

2. Avant d'exécuter le programme Python, vous devez vous assurer que vous êtes dans le bon répertoire. Tapez la commande suivante dans le terminal :

   ```bash
   cd ~/project
   ```

   Cette commande change le répertoire de travail actuel pour le répertoire `project` dans votre répertoire personnel.

3. Une fois que vous êtes dans le bon répertoire, vous pouvez exécuter votre programme Python. Tapez la commande suivante dans le terminal :

   ```bash
   python3 hello.py
   ```

   Cette commande indique à l'interpréteur Python d'exécuter le fichier `hello.py`.

4. Lorsque le programme s'exécute, il vous demandera d'entrer votre nom. Tapez votre nom et appuyez sur Entrée.

5. Après avoir appuyé sur Entrée, vous devriez voir une sortie similaire à :

   ```
   Enter your name: John
   Hello, John! Welcome to Python programming.
   ```

   La sortie réelle affichera le nom que vous avez saisi au lieu de "John".

Ce simple programme démontre plusieurs concepts importants en Python :

- Créer un fichier Python : Vous avez appris à créer un nouveau fichier Python dans le WebIDE.
- Ajouter des commentaires : Les commentaires sont utilisés pour expliquer le code et le rendre plus compréhensible.
- Obtenir des entrées de l'utilisateur avec la fonction `input()` : Cette fonction permet à votre programme d'interagir avec l'utilisateur.
- Utiliser des variables pour stocker des données : Les variables sont utilisées pour stocker des valeurs qui peuvent être utilisées plus tard dans le programme.
- Afficher une sortie avec la fonction `print()` : Cette fonction est utilisée pour afficher des informations à l'écran.
- Utiliser des f-strings pour le formatage de chaînes de caractères : Les f-strings offrent un moyen pratique d'insérer des variables dans des chaînes de caractères.
