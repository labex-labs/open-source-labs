# Voir les différences dans les modifications

En tant que développeur, vous pouvez vouloir voir les différences entre vos modifications préparées ou non et le dernier commit. Cela est utile lorsque vous voulez réviser vos modifications avant de les commettre ou lorsque vous voulez voir quelles modifications vous avez apportées depuis le dernier commit.

## Tâches

Pour démontrer comment voir les différences dans les modifications, nous utiliserons le référentiel `git-playground`. Supposons que vous avez apporté quelques modifications au fichier `README.md` et que vous voulez voir les différences entre vos modifications et le dernier commit.

1. Ouvrez votre terminal et accédez au répertoire `git-playground`.
2. Voir les différences entre vos modifications non préparées et le dernier commit.
3. Voir les différences entre vos modifications préparées et le dernier commit.

Voici le résultat de l'achèvement de l'étape 2 :

```
diff --git a/file1.txt b/file1.txt
index bfccc4a..ee23125 100644
--- a/file1.txt
+++ b/file1.txt
@@ -1 +1,2 @@
 This is file1.
+hello,labex
```

Voici le résultat de l'achèvement de l'étape 3 :

```
diff --git a/README.md b/README.md
index 0164284..f47591b 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,3 @@
 # git-playground
 Git Playground
+hello,world
```
