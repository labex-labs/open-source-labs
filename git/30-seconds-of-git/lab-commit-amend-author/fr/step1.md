# Changer l'auteur du dernier commit

Vous venez de faire un commit dans votre référentiel Git, mais vous vous êtes rendu compte que le nom et l'adresse e-mail de l'auteur sont incorrects. Vous voulez mettre à jour les informations de l'auteur sans modifier le contenu du commit. Comment pouvez-vous le faire avec Git?

Pour changer l'auteur du dernier commit, vous pouvez utiliser la commande `git commit --amend`. Cette commande vous permet de modifier le dernier commit de votre référentiel Git. Voici un exemple de la manière dont vous pouvez changer le nom et l'adresse e-mail de l'auteur :

1. Clonez le référentiel Git nommé `https://github.com/labex-labs/git-playground` sur votre machine locale :

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Configurez les informations d'identité de Git à l'aide de votre compte GitHub :

```shell
cd git-playground
git config user.email "votre adresse e-mail"
git config user.name "votre nom d'utilisateur"
```

3. Utilisez la commande `git commit --amend` pour modifier l'auteur du dernier commit et enregistrer le contenu :

```shell
git commit --amend --author="Duck Quackers <cool.duck@qua.ck>"
```

4. Vérifiez que les informations de l'auteur ont été mises à jour :

```shell
git log
```

Vous devriez voir que l'auteur du dernier commit est désormais `Duck Quackers` :

```shell
commit d5a385cc354f3528472a215b66cbb7c628ba47d5
Author: Duck Quackers <cool.duck@qua.ck>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
