# Créer un commit de correction

Supposons que vous travailliez sur un projet avec plusieurs autres développeurs et que vous remarquezv une petite erreur dans un commit effectué il y a quelques jours. Vous voulez corriger l'erreur, mais vous ne voulez pas créer un nouveau commit et perturber le travail des autres développeurs. C'est là que les commits de correction s'avèrent utiles. En créant un commit de correction, vous pouvez apporter les modifications nécessaires sans créer un nouveau commit, et le commit de correction sera automatiquement fusionné avec le commit original lors de la prochaine rebase.

## Tâches

Votre tâche consiste à écrire la chaîne de caractères "hello,world" dans le fichier `hello.txt` et à l'ajouter en tant que commit de "correction" au commit avec le message "Added file1.txt", de manière à ce qu'il puisse être automatiquement fusionné lors d'une opération de rebase ultérieure.

Pour ce défi, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Accédez au répertoire et configurez l'identité.
2. Créez un fichier `hello.txt`, écrivez "hello,world" dedans et ajoutez-le à la zone de préparation.
3. Créez un commit de correction pour le hachage du message de commit "Added file1.txt".
4. Une fois que vous avez créé le commit de correction, vous pouvez automatiquement fusionner le commit de correction avec le commit original lors de la prochaine rebase. Lorsque vous ouvrez l'éditeur interactif, vous n'avez pas besoin de modifier le texte et d'enregistrer pour quitter.

Voici le résultat de l'exécution de la commande `git show HEAD~1` :

```shell

```
