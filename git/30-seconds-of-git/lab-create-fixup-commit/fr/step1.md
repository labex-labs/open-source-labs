# Créer un commit de correction

Supposons que vous travailliez sur un projet avec plusieurs autres développeurs et que vous remarquez une petite erreur dans un commit effectué il y a quelques jours. Vous voulez corriger l'erreur, mais vous ne voulez pas créer un nouveau commit et perturber le travail des autres développeurs. C'est là que les commits de correction s'avèrent utiles. En créant un commit de correction, vous pouvez apporter les modifications nécessaires sans créer un nouveau commit, et le commit de correction sera automatiquement fusionné avec le commit original lors du prochain rebase.

Par exemple, votre tâche est d'écrire la chaîne "hello,world" dans le fichier `hello.txt` et de l'ajouter en tant que commit de "correction" au commit avec le message "Ajouté file1.txt", de manière à ce qu'il puisse être automatiquement fusionné lors d'une opération de rebase ultérieure.

Pour ce laboratoire, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Clonez le référentiel, accédez au répertoire et configurez l'identité :

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "votre-nom-d'utilisateur"
git config --global user.email "votre-adresse-email"
```

2. Créez un fichier `hello.txt`, écrivez "hello,world" dedans et ajoutez-le à la zone de préparation :

```shell
echo "hello,world" > hello.txt
git add.
```

3. Pour créer un commit de correction, vous pouvez utiliser la commande `git commit --fixup <commit>` :

```shell
git commit --fixup cf80005
# Ceci est le hash du commit avec le message "Ajouté file1.txt".
```

Cela créera un commit de correction pour le commit spécifié. Notez que vous devez préparer vos modifications avant de créer le commit de correction. 4. Une fois que vous avez créé le commit de correction, vous pouvez utiliser la commande `git rebase --interactive --autosquash` pour fusionner automatiquement le commit de correction avec le commit original lors du prochain rebase. Par exemple :

```shell
git rebase --interactive --autosquash HEAD~3
```

Lorsque vous ouvrez l'éditeur interactif, vous n'avez pas besoin de modifier le texte et de le sauvegarder pour sortir. Cela effectuera un rebase sur les 3 derniers commits et fusionnera automatiquement tout commit de correction avec son commit original correspondant.

Voici le résultat de l'exécution de la commande `git show HEAD~1` :

```shell
commit 6f0b8bbfac939af197a44ecd287ef84153817e9d
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

diff --git a/file1.txt b/file1.txt
new file mode 100644
index 0000000..bfccc4a
--- /dev/null
+++ b/file1.txt
@@ -0,0 +1 @@
+This is file1.
diff --git a/hello.txt b/hello.txt
new file mode 100644
index 0000000..2d832d9
--- /dev/null
+++ b/hello.txt
@@ -0,0 +1 @@
+hello,world
```
