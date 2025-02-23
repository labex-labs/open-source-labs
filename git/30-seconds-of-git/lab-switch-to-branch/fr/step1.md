# Basculer vers une branche

Vous avez travaillé sur un projet dans un référentiel Git nommé `https://github.com/labex-labs/git-playground`. Votre équipe a créé une nouvelle branche nommée `feature-1` pour travailler sur une nouvelle fonctionnalité. Vous devez basculer vers la branche `feature-1` pour continuer à travailler sur la fonctionnalité.

1. Clonez le référentiel Git :

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Accédez au répertoire du référentiel :

```shell
cd git-playground
```

3. Liste toutes les branches dans le référentiel :

```shell
git branch
```

Sortie :

```shell
feature-1
* master
```

4. Basculez vers la branche `feature-1` :

```shell
git checkout feature-1
```

Sortie :

```shell
Switched to branch 'feature-1'
```

5. Vérifiez que vous êtes maintenant sur la branche `feature-1` :

```shell
git branch
```

Sortie :

```shell
* feature-1
master
```
