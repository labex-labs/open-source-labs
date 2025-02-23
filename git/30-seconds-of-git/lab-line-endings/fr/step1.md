# Configure les sauts de ligne

Vous travaillez sur un projet avec une équipe de développeurs et vous remarquez que certains membres de l'équipe utilisent des sauts de ligne différents des autres. Cela peut entraîner des problèmes lors de la fusion du code et peut mener à des conflits. Vous devez configurer les sauts de ligne pour le référentiel afin d'assurer la cohérence et d'éviter les conflits.

Sur les systèmes Unix ou Unix-like, chaque ligne de texte se termine par le terminateur de ligne `LF` (Line Feed). Lorsque vous utilisez la commande `cat` pour afficher un fichier, les terminateurs de ligne ne sont normalement pas affichés à l'écran car ils sont considérés comme la fin de la ligne, et non pas comme une partie de la ligne.

Lorsque vous affichez un fichier avec la commande `cat -vet`, l'option `-v` affiche les caractères non imprimables sous forme de séquences de caractères visibles, telles que le symbole `$`. Par conséquent, si vous voyez le symbole `$` dans un fichier, cela signifie que chaque ligne du fichier se termine par le terminateur de ligne `LF`. `LF` et `\n` sont le même concept, indiquant un terminateur de ligne.

Pour configurer les sauts de ligne pour le référentiel `git-playground`, suivez ces étapes :

1. Ouvrez l'invite de commande ou le terminal de votre ordinateur.
2. Accédez au répertoire où se trouve le référentiel `git-playground` dans le répertoire `~/project`.
3. Exécutez la commande suivante pour configurer les sauts de ligne pour utiliser les sauts de ligne UNIX :

   ```shell
   git config core.eol lf
   ```

   Cela configurera les sauts de ligne pour utiliser le saut de ligne UNIX (`\n`).

4. Exécutez la commande suivante pour vérifier que les sauts de ligne ont été correctement configurés :

   ```shell
   git config core.eol
   ```

   Cela affichera la configuration actuelle des sauts de ligne.

Voici le résultat de l'exécution de `cat -vet file2.txt` :

```shell
This is file2.$
```
