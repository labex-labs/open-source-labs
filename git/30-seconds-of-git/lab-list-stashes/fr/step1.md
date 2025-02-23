# Lister tous les stockages temporaires

Vous travaillez sur un projet dans un référentiel Git et avez effectué certaines modifications qui ne sont pas encore prêtes à être validées. Vous décidez de stocker temporairement ces modifications pour pouvoir travailler sur une autre tâche. Plus tard, vous voulez voir la liste de tous les stockages temporaires que vous avez créés pour pouvoir décider lequel appliquer. Comment lister tous les stockages temporaires dans un référentiel Git?

1. Accédez au répertoire `git-playground` :

```
cd git-playground
```

2. Créez un nouveau fichier nommé `test.txt` et ajoutez-y du contenu :

```
echo "hello,world" > test.txt
git add.
```

3. Utilisez la commande suivante pour stocker temporairement vos modifications :

```
git stash save "Added test.txt"
```

4. Créez un autre nouveau fichier nommé `test2.txt` et ajoutez-y du contenu :

```
echo "hello,labex" > test2.txt
git add.
```

5. Utilisez la commande suivante pour stocker temporairement vos modifications :

```
git stash save "Added test2.txt"
```

6. Utilisez la commande suivante pour lister tous les stockages temporaires :

```
git stash list
```

Vous devriez voir une sortie similaire à la suivante :

```
stash@{0}: On master: Added test2.txt
stash@{1}: On master: Added test.txt
```
