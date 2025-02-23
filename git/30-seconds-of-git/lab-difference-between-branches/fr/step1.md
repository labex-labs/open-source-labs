# Différence entre les branches

Vous avez travaillé sur un projet avec votre équipe et vous avez créé une branche nommée `feature-1` pour travailler sur une nouvelle fonctionnalité. Votre collègue a également créé une branche nommée `feature-2` pour travailler sur une fonctionnalité différente. Vous voulez comparer les modifications entre les deux branches pour voir ce qui a été ajouté, modifié ou supprimé. Comment pouvez-vous visualiser la différence entre les deux branches?

Supposons que votre compte GitHub clone un référentiel appelé `git-playground` à partir de `https://github.com/labex-labs/git-playground.git`. Suivez les étapes suivantes :

1. Changez de répertoire vers le référentiel en utilisant la commande `cd git-playground`.
2. Configurez votre compte GitHub dans cet environnement en utilisant les commandes `git config --global user.name "Votre Nom"` et `git config --global user.email "votre@email.com"`.
3. Créez et basculez sur la branche `feature-1` en utilisant la commande `git checkout -b feature-1`, ajoutez "hello" au fichier `README.md`, ajoutez-le à la zone de préparation et validez, le message de validation est "Ajoutez du nouveau contenu au README.md" en utilisant les commandes `echo "hello" >> README.md `, `git add.` et `git commit -am "Ajoutez du nouveau contenu au README.md"`.
4. Revenez sur la branche `master`.
5. Créez et basculez sur la branche `feature-2` en utilisant la commande `git checkout -b feature-2`, ajoutez "world" au fichier `index.html`, ajoutez-le à la zone de préparation et validez, le message de validation est "Mettez à jour le fichier index.html" en utilisant les commandes `echo "world" > index.htm`, `git add.` et `git commit -am "Mettez à jour le fichier index.html"`.
6. Visualisez la différence entre les deux branches en utilisant la commande `git diff feature-1..feature-2`.

La sortie devrait afficher la différence entre les branches `feature-1` et `feature-2`. Voici comment le résultat final devrait ressembler :

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
