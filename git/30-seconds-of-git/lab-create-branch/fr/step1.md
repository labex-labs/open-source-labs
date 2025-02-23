# Créer une nouvelle branche

Pour ce laboratoire, clonez le référentiel Git nommé `https://github.com/labex-labs/git-playground` dans votre compte GitHub. Vous travaillez sur un projet dans un référentiel Git nommé `https://github.com/your-username/git-playground`. Vous devez créer une nouvelle branche nommée `feature-1` pour travailler sur une nouvelle fonctionnalité.

1. Clonez le référentiel, accédez au répertoire et configurez l'identité :

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Vérifiez la branche actuelle :

```shell
git branch
```

3. Créez une nouvelle branche nommée `feature-1` :

```shell
git checkout -b feature-1
```

4. Vérifiez que vous êtes maintenant sur la branche `feature-1` :

```shell
git branch
```

5. Poussez les modifications vers le référentiel distant :

```shell
git push -u origin feature-1
```

Voici ce qui se passe lorsque vous exécutez la commande `git branch -r` :

![git branch remote output](../assets/challenge-create-branch-step1-1.png)
