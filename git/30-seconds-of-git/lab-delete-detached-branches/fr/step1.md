# Supprimer les branches détachées

Vous disposez d'un référentiel Git avec plusieurs branches détachées que vous n'avez plus besoin. Ces branches encombrent votre référentiel et le rendent difficile à gérer. Vous souhaitez supprimer toutes les branches détachées pour nettoyer votre référentiel.

Pour terminer ce laboratoire, vous utiliserez le référentiel Git `git-playground` de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`. Ne cochez pas "Copier seulement la branche master".

1. Clonez le référentiel, accédez au répertoire et configurez l'identité :

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Puisque la branche `feature-branch` existe dans le référentiel distant, basculez vers `feature-branch`, ce qui fera en sorte que la branche `feature-branch` locale suive la branche `feature-branch` du référentiel distant et supprime la branche `feature-branch` dans le référentiel distant :

```shell
git checkout feature-branch
git push origin --delete feature-branch
```

3. Affichez la relation de suivi entre les branches locales et les branches distantes qu'elles suivent :

```shell
git branch -vv
```

4. Revenez sur la branche `master` :

```shell
git checkout master
```

5. Supprimez toutes les branches détachées de votre référentiel local :

```shell
git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
```

6. Vérifiez que les branches détachées ont été supprimées :

```shell
git branch
```

La sortie devrait ne montrer que les branches associées à une branche spécifique :

```shell
* master d22f46b [origin/master] Added file2.txt
```
