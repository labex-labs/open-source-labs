# Retour à la branche précédente

En tant que développeur, vous travaillez sur un projet et avez basculé sur une branche différente pour travailler sur une nouvelle fonctionnalité. Après avoir apporté quelques modifications, vous réalisez que vous devez revenir à la branche précédente pour corriger un bogue. Vous pouvez commettre vos modifications dans une nouvelle branche et utiliser une commande pour basculer rapidement vers la branche précédente.

Pour démontrer comment revenir à la branche précédente, nous utiliserons le référentiel Git nommé `https://github.com/labex-labs/git-playground`. Suivez les étapes ci-dessous :

1. Clonez le référentiel en utilisant la commande suivante :
   ```
   git clone https://github.com/labex-labs/git-playground.git
   ```
2. Changez de répertoire vers le répertoire du référentiel :
   ```
   cd git-playground
   ```
3. Créez une nouvelle branche nommée `feature-branch` :
   ```
   git checkout -b feature-branch
   ```
4. Vérifiez la branche actuelle et basculez rapidement vers la branche précédente. Le nom de votre nouvelle branche est `feature-branch` et le nom de la branche précédente vers laquelle vous voulez revenir est `master` :
   ```
   git checkout -
   ```
   Cela vous ramènera à la branche `master`, et vos modifications seront toujours là.
