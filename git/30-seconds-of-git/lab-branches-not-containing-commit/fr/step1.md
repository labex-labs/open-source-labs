# Trouver les branches ne contenant pas un commit

Vous travaillez sur un projet avec plusieurs branches, et vous devez trouver toutes les branches qui ne contiennent pas un commit spécifique. Cela peut être utile si vous voulez vous assurer qu'un certain changement a été appliqué à toutes les branches, ou si vous voulez savoir quelles branches sont obsolètes et doivent être mises à jour.

Pour ce laboratoire, nous allons utiliser le référentiel Git nommé `https://github.com/your-username/git-playground`.

1. Clonez ce référentiel sur votre machine locale en utilisant la commande suivante :

```shell
git clone https://github.com/your-username/git-playground.git
```

2. Après avoir cloné le référentiel, utilisez les commandes suivantes pour naviguer dans le répertoire et configurer l'identité :

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Créez et basculez sur une branche `new-branch` et apportez quelques modifications de code sur cette branche puis committez-les, le message de commit est "Créer une branche new-branch" :

```shell
git checkout -b new-branch
echo "hello,world" > file1.txt
git commit -am "Créer une branche new-branch"
```

4. Vérifiez le hash du message de commit "Créer une branche new-branch" :

```shell
git log
```

5. Trouvez toutes les branches qui ne contiennent pas un hash avec le message de commit "Créer une branche new-branch". Pour ce faire, nous pouvons utiliser la commande suivante :

```shell
git branch --no-contains 31c5ac20129151af1
```

Cela affichera une liste de toutes les branches qui ne contiennent pas le commit spécifié. Dans ce cas, la sortie sera :

```shell
master
```

Cela signifie que la branche `master` ne contient pas le commit avec le hash `31c5ac20129151af1`.
