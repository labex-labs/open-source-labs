# Purge a file from history

Supposons que vous ayez accidentellement commité un fichier contenant des informations sensibles, telles que des clés API ou des mots de passe, dans votre référentiel Git. Vous réalisez que ce fichier n'aurait jamais dû être commité et que vous voulez le supprimer complètement de l'historique du référentiel. Cependant, simplement supprimer le fichier et commettre le changement ne le supprimera pas de l'historique du référentiel. Le fichier sera toujours accessible dans les commits précédents, ce qui pourrait représenter un risque de sécurité.

## Tâches

Pour terminer ce défi, vous utiliserez le référentiel Git `git-playground` de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`. Ce référentiel contient un fichier nommé `file1.txt` qui n'aurait jamais dû être commité. Veuillez purger `file1.txt` de l'historique du référentiel.

1. Clonez le référentiel sur votre machine locale à partir de `https://github.com/your-username/git-playground`.
2. Accédez au répertoire et configurez l'identité.
3. Supprimez le fichier de l'index du référentiel.
4. Rédigez à nouveau l'historique du référentiel, en supprimant toutes les instances de `file1.txt`.
5. Poussez les modifications vers le référentiel distant en forçant.

Après avoir effectué ces étapes, `file1.txt` sera complètement supprimé de l'historique du référentiel et après avoir exécuté `git log --remotes`, vous ne verrez pas le commit sur `file1.txt`.
