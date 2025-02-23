# Copier un fichier d'une autre branche

Vous travaillez sur un projet dans un référentiel Git nommé `https://github.com/labex-labs/git-playground.git`. Vous avez deux branches nommées `feature-1` et `feature-2`. Vous devez copier le fichier `hello.txt` de la branche `feature-1` vers la branche `feature-2`.

## Tâches

1. Accédez au répertoire et configurez l'identité.
2. Créez et basculez sur la branche `feature-1` et créez un fichier texte nommé `hello.txt` et écrivez la chaîne "hello,world" dedans et validez le fichier avec le message "add hello.txt".
3. Créez et basculez sur la branche `feature-2` après avoir basculé sur la branche `master`.
4. Copiez le fichier `hello.txt` de la branche `feature-1` vers la branche `feature-2` et validez-le avec le message de validation "copy hello.txt".
5. Vérifiez que le fichier `hello.txt` a été copié dans la branche `feature-2`.

Vous devriez voir le fichier `hello.txt` dans la liste des fichiers de la branche `feature-2` :

```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
