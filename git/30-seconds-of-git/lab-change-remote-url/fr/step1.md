# Change the Remote URL

Vous avez cloné un référentiel depuis GitHub et apporté quelques modifications. Cependant, vous réalisez maintenant que vous devez modifier l'URL du référentiel distant. Cela peut être parce que le référentiel original a été déplacé vers un autre emplacement, ou parce que vous voulez pousser vos modifications vers un autre référentiel distant. Votre tâche consiste à modifier l'URL du référentiel distant à l'aide de commandes Git.

Vous devrez cloner le référentiel `https://github.com/labex-labs/git-playground` sur votre machine locale. Pour modifier l'URL du référentiel distant en `https://github.com/your-username/git-playground`, suivez ces étapes :

1. Ouvrez un terminal ou une invite de commande, clonez le référentiel et accédez au référentiel local.
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```
2. Utilisez la commande suivante pour afficher l'URL du référentiel distant actuelle :
   ```
   git remote -v
   ```
3. Utilisez la commande suivante pour modifier l'URL du référentiel distant en la nouvelle URL :
   ```
   git remote set-url origin https://github.com/your-username/git-playground
   ```
4. Utilisez la commande suivante pour vérifier que l'URL du référentiel distant a été modifiée :
   ```
   git remote -v
   ```

La sortie devrait montrer la nouvelle URL au lieu de l'ancienne :

![Updated remote URL output](../assets/challenge-change-remote-url-step1-1.png)
