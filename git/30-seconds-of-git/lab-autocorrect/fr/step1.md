# Autocorrect Git Commands

Le problème est que les développeurs tapent souvent mal les commandes git, ce qui peut entraîner des erreurs et ralentir leur flux de travail. Par exemple, un développeur peut accidentellement taper `git sttaus` au lieu de `git status`, ce qui entraînera un message d'erreur. Cela peut être frustrant et consommer du temps, en particulier lorsqu'on travaille sur de grands projets avec de nombreux fichiers et collaborateurs.

Pour démontrer comment utiliser la fonction d'autocorrection de Git, nous utiliserons le référentiel git nommé `https://github.com/labex-labs/git-playground` dans le répertoire.

1. Ouvrez votre terminal et accédez au répertoire où vous voulez cloner le référentiel.
2. Clonez le référentiel en utilisant la commande suivante :

```
git clone https://github.com/labex-labs/git-playground.git
```

3. Accédez au référentiel cloné en utilisant la commande suivante :

```
cd git-playground
```

4. Activez la fonction d'autocorrection de Git en utilisant la commande suivante :

```
git config --global help.autocorrect 1
```

5. Essayez de mal taper une commande git, telle que `git sttaus`. Git corrigera automatiquement la commande et exécutera `git status` à la place.

Voici le résultat après avoir terminé le laboratoire :

![Git autocorrect command result](../assets/challenge-autocorrect-step1-1.jpg)
