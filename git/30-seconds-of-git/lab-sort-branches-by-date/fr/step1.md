# Trier les branches Git par date

Vous disposez d'un référentiel Git avec plusieurs branches, et vous souhaitez les trier par date. Cela vous permettra de voir quelles branches ont été mises à jour récemment et lesquelles ne l'ont pas été. Trier les branches par date peut également vous aider à identifier les branches qui peuvent nécessiter une attention ou un regroupement.

Pour ce laboratoire, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Clonez le référentiel sur votre machine locale :

```shell
git clone https://github.com/labex-labs/git-playground
```

2. Accédez au répertoire du référentiel et configurez votre identité GitHub :

```shell
cd git-playground
git config --global user.name "votre-nom-d'utilisateur"
git config --global user.email "votre-email"
```

3. Créez une branche appelée `one`, modifiez le code et validez les modifications :

```shell
git checkout -b one
touch hello.txt
git add.
git commit -m "hello.txt"
```

4. Basculez sur la branche `master` et créez une branche nommée `two` :

```shell
git checkout master
git checkout -b two
```

5. Maintenant, pour trier les branches par date, utilisez la commande suivante :

```shell
git branch --sort=-committerdate
```

Cela affichera une liste de toutes les branches locales et les triera en fonction de la date de leur dernier commit. Vous pouvez utiliser les flèches du clavier pour naviguer dans la liste et appuyer sur <kbd>Q</kbd> pour sortir.

Voici le résultat final :

![liste de branches Git triées](../assets/challenge-sort-branches-by-date.png)
