# Clonage du dépôt Git

Pour commencer à explorer les capacités de filtrage par plage de dates de Git, nous avons d'abord besoin d'un dépôt Git sur lequel travailler. Nous allons utiliser le dépôt `git-playground` fourni par LabEx.

Commençons par cloner le dépôt :

1. Ouvrez votre terminal dans la machine virtuelle (VM) LabEx.

![terminal](../assets/screenshot-20250306-shbu3WrQ@2x.png)

2. Exécutez la commande suivante pour cloner le dépôt :

```bash
git clone https://github.com/labex-labs/git-playground
```

Vous devriez voir une sortie similaire à celle-ci :

```
Cloning into 'git-playground'...
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 8 (delta 0), reused 8 (delta 0), pack-reused 0
Receiving objects: 100% (8/8), done.
```

3. Accédez au répertoire du dépôt :

```bash
cd git-playground
```

Maintenant que nous avons le dépôt sur notre machine locale, nous pouvons commencer à explorer l'historique des commits (validations).
