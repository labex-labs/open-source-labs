# Exploration de la commande de base `git log`

Maintenant que nous avons cloné notre dépôt, apprenons à afficher l'historique des commits (validations) en utilisant la commande `git log`.

La commande `git log` affiche une liste de tous les commits du dépôt, en commençant par le plus récent. Chaque entrée de commit comprend :

- Un hachage de commit unique (identifiant)
- Des informations sur l'auteur
- La date et l'heure du commit
- Le message de commit

Affichons l'historique de base des commits :

```bash
git log
```

Vous devriez voir une sortie similaire à ce qui suit :

```
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```

Si la sortie est longue, vous pouvez la parcourir en utilisant :

- Appuyez sur `Espace` pour avancer
- Appuyez sur `b` pour reculer
- Appuyez sur `q` pour quitter la vue du journal

Notez que chaque commit a un identifiant unique (la longue chaîne hexadécimale), les informations de l'auteur, la date et l'heure du commit, ainsi qu'un message décrivant les modifications apportées.
