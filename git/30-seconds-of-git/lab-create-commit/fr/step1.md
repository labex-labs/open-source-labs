# Créer un commit Git

Vous avez apporté quelques modifications à votre code et vous voulez les enregistrer sous forme d'un instantané dans votre référentiel Git. Cependant, vous ne voulez pas enregistrer toutes les modifications que vous avez effectuées, seulement celles qui sont pertinentes pour la fonctionnalité actuelle ou la correction de bogue. Comment pouvez-vous créer un commit ne contenant que les modifications pertinentes?

Pour ce laboratoire, utilisons le référentiel de `https://github.com/labex-labs/git-playground`, suivez ces étapes :

1. Clonez le référentiel et accédez-y :

   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```

2. Configurez votre compte github dans l'environnement :

   ```
   git config --global user.name "votre-nom"
   git config --global user.email "votre-email"
   ```

3. Ajoutez "hello,labex" au fichier `README.md`, ajoutez-le à la zone de préparation et validez-le avec le message "Mettre à jour README.md" :

   ```
   echo "hello,labex" >> README.md
   git add.
   git commit -m "Mettre à jour README.md"
   ```

   L'option `-m` vous permet de spécifier un message de commit. Assurez-vous que le message est descriptif et explique quelles modifications le commit contient.

Voici le résultat de l'exécution de la commande `git log` :

![Résultat de la commande git log](../assets/challenge-create-commit-step1-1.png)
