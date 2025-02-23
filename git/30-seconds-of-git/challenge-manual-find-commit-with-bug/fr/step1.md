# Trouver manuellement le commit qui a introduit un bogue

Votre tâche consiste à trouver manuellement le commit qui a introduit un bogue dans le référentiel `git-playground`. Le référentiel est disponible à l'adresse `https://github.com/labex-labs/git-playground`.

Pour accomplir ce défi, vous devrez effectuer une recherche dichotomique dans l'historique des commits du référentiel. Vous devrez marquer les commits comme étant soit "bons" (sans bogue) soit "mauvais" (ayant un bogue) jusqu'à ce que vous ayez réduit l'emprise sur le commit qui a introduit le bogue.

## Tâches

Le message d'erreur est que le fichier `file2.txt` devrait afficher "This is file2.txt." au lieu de "This is file2.".

1. Accédez au répertoire du référentiel.
2. Démarrez une recherche dichotomique.
3. Marquez le commit actuel comme "mauvais".
4. Marquez un commit avec le message "Initial commit" comme "bon". Git vous décheckoutera automatiquement un nouveau commit pour le tester.
5. Si le contenu du fichier `file2.txt` vérifié ne correspond pas au bogue, marquez-le comme "bon".
6. Si le contenu du fichier `file2.txt` vérifié correspond au bogue, marquez-le comme "mauvais".
7. Une fois que vous avez trouvé le commit ayant le bogue, quittez la recherche dichotomique.

Vous pouvez maintenant examiner les modifications de code dans le commit ayant le bogue pour trouver la source du bogue.

Voici le résultat du test :

```
d22f46ba8c2d4e07d773c5126e9c803933eb5898 est le premier commit ayant un bogue
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

 file2.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 file2.txt
```
