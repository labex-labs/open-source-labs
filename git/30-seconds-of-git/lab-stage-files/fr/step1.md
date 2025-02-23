# Ajouter des fichiers à la zone de préparation

Vous avez travaillé sur un projet stocké dans un référentiel Git nommé `https://github.com/labex-labs/git-playground`. Vous avez apporté quelques modifications à la base de code et vous souhaitez commettre ces modifications dans le référentiel. Cependant, vous ne voulez commettre que des modifications spécifiques et pas toutes les modifications que vous avez effectuées. Pour ce faire, vous devez ajouter les fichiers à la zone de préparation.

1. Vous allez effectuer quelques modifications dans le répertoire `git-playground` :

```shell
echo "hello" > index.html
echo "world" > style.css
echo "git" > one.js
echo "labex" > two.js
echo "hello git" > 1.py
echo "hello labex" > 2.py
```

2. Ajoutez ces fichiers à la zone de préparation :

```shell
git add index.html style.css
```

3. Affichez l'état du répertoire de travail actuel et de la zone de préparation, y compris des informations sur les fichiers modifiés, les fichiers ajoutés à la zone de préparation, etc. :

```shell
git status
```

4. Alternativement, ajoutez tous les fichiers avec une extension `.js` :

```shell
git add *.js
```

5. Affichez à nouveau l'état du répertoire de travail actuel et de la zone de préparation :

```shell
git status
```

6. Vous pouvez également ajouter toutes les modifications à la zone de préparation :

```shell
git add.
```

7. Affichez à nouveau l'état du répertoire de travail actuel et de la zone de préparation :

```shell
git status
```

Voici le résultat final :

![Git staging area status](../assets/challenge-stage-files-step1-1.png)
