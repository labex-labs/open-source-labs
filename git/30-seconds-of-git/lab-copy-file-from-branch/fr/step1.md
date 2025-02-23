# Copier un fichier d'une autre branche

Vous travaillez sur un projet dans un référentiel Git nommé `https://github.com/labex-labs/git-playground.git`. Vous avez deux branches nommées `feature-1` et `feature-2`. Vous devez copier le fichier `hello.txt` de la branche `feature-1` vers la branche `feature-2`.

1. Cloner le référentiel :

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Naviguer dans le répertoire et configurer l'identité :

```shell
cd git-playground
git config --global user.name "votre-nom-d'utilisateur"
git config --global user.email "votre-email"
```

3. Créer et basculer sur la branche `feature-1` et créer un fichier texte nommé `hello.txt` et y écrire la chaîne "hello,world" puis committer le fichier avec le message "add hello.txt" :

```shell
git checkout -b feature-1
echo "hello,world" > hello.txt
git add.
git commit -m "add hello.txt"
```

4. Créer et basculer sur la branche `feature-2` après avoir basculé sur la branche `master` :

```shell
git checkout master
git checkout -b feature-2
```

5. Copier le fichier `hello.txt` de la branche `feature-1` vers la branche `feature-2` et le committer avec le message de commit "copy hello.txt" :

```shell
git checkout feature-1 hello.txt
git commit -am "copy hello.txt"
```

6. Vérifier que le fichier `hello.txt` a été copié dans la branche `feature-2` :

```shell
ll
```

Vous devriez voir le fichier `hello.txt` dans la liste des fichiers de la branche `feature-2` :

```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
