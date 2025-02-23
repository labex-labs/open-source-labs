# Purge a file from history

Supposons que vous ayez accidentellement commis un fichier contenant des informations sensibles, telles que des clés API ou des mots de passe, dans votre référentiel Git. Vous réalisez que ce fichier n'aurait jamais dû être commis et que vous voulez le supprimer complètement de l'historique du référentiel. Cependant, simplement supprimer le fichier et commettre le changement ne le supprimera pas de l'historique du référentiel. Le fichier sera toujours accessible dans les commits précédents, ce qui pourrait représenter un risque de sécurité.

Pour terminer ce laboratoire, vous utiliserez le référentiel Git `git-playground` de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`. Ce référentiel contient un fichier nommé `file1.txt` qui n'aurait jamais dû être commis. Pour purger `file1.txt` de l'historique du référentiel, suivez ces étapes :

1. Clonez le référentiel sur votre machine locale :

```shell
git clone https://github.com/your-username/git-playground
```

2. Utilisez les commandes suivantes pour naviguer dans le répertoire et configurer l'identité :

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Supprimez le fichier de l'index du référentiel.

```shell
git rm --cached --ignore-unmatch file1.txt
```

4. Commettez ce changement avec le message de commit "Remove sensitive file1.txt" :

```shell
git commit -m "Remove sensitive file1.txt"
```

5. Rédigez à nouveau l'historique du référentiel, en supprimant toutes les instances de `file1.txt` :

```shell
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch file1.txt" --prune-empty --tag-name-filter cat -- --all
```

6. Poussez les changements vers le référentiel distant en forçant :

```shell
git push origin --force --all
```

Après avoir effectué ces étapes, `file1.txt` sera complètement supprimé de l'historique du référentiel et après avoir exécuté `git log --remotes`, vous ne verrez pas le commit sur `file1.txt`.
