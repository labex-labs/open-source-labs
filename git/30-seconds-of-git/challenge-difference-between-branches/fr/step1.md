# Différence entre les branches

Vous avez travaillé sur un projet avec votre équipe et vous avez créé une branche nommée `feature-1` pour travailler sur une nouvelle fonctionnalité. Votre collègue a également créé une branche nommée `feature-2` pour travailler sur une fonctionnalité différente. Vous voulez comparer les modifications entre les deux branches pour voir ce qui a été ajouté, modifié ou supprimé. Comment pouvez-vous visualiser la différence entre les deux branches?

## Tâches

Supposons que votre compte GitHub clone un référentiel appelé `git-playground` à partir de `https://github.com/labex-labs/git-playground.git`.

1. Accédez au répertoire du référentiel et configurez votre identité GitHub.
2. Basculez sur la branche `feature-1` et ajoutez "hello" au fichier `README.md`, ajoutez-le à la zone de préparation et validez, le message de validation est "Ajoutez de nouveau contenu au README.md".
3. Basculez sur la branche `feature-2` et ajoutez "world" au fichier `index.html`, ajoutez-le à la zone de préparation et validez, le message de validation est "Mettez à jour le fichier index.html".
4. Visualisez la différence entre les deux branches.

La sortie devrait afficher la différence entre les branches `feature-1` et `feature-2`. Voici à quoi ressemblera le résultat final :

```shell
diff --git a/README.md b/README.md
index b66215f..0164284 100644
--- a/README.md
+++ b/README.md
@@ -1,3 +1,2 @@
# git-playground
Git Playground
-hello
diff --git a/index.html b/index.html
new file mode 100644
index 0000000..cc628cc
--- /dev/null
+++ b/index.html
@@ -0,0 +1 @@
+world
```
