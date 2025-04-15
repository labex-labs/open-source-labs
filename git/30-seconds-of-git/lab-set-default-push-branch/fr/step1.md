# Définir le nom de la branche de poussée par défaut

Lorsque vous poussez des modifications vers un référentiel distant, Git utilisera le nom de la branche locale actuelle comme nom par défaut pour la branche distante. Cependant, parfois vous souhaiterez peut-être pousser vos modifications vers une autre branche. Dans ce cas, vous devrez spécifier explicitement le nom de la branche distante chaque fois que vous poussez vos modifications. Cela peut être fastidieux et propice à des erreurs, en particulier si vous travaillez avec plusieurs branches.

Pour terminer ce laboratoire, vous utiliserez le référentiel Git `git-playground` de votre compte GitHub, qui provient d'un fork de `https://github.com/labex-labs/git-playground.git`. Suivez les étapes ci-dessous pour définir le nom de la branche de poussée par défaut :

1. Clonez le référentiel en utilisant la commande suivante :
   ```
   git clone https://github.com/your-username/git-playground.git
   ```
2. Changez de répertoire vers le répertoire du référentiel :
   ```
   cd git-playground
   ```
3. Définissez le nom de la branche de poussée par défaut sur le nom de la branche locale actuelle :
   ```
   git config push.default current
   ```
4. Créez une nouvelle branche et basculez vers elle :
   ```
   git checkout -b my-branch
   ```
5. Apportez quelques modifications au référentiel et committez-les :
   ```
   echo "Hello, World" > hello.txt
   git add hello.txt
   git commit -m "Add hello.txt"
   ```
6. Poussez vos modifications vers le référentiel distant :
   ```
   git push -u
   ```
   Git poussera vos modifications vers une branche nommée `my-branch` sur le référentiel distant.

Voici le résultat de l'exécution de `git log` :

```shell
ADD hello.txt
```
