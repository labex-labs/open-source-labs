# Modifier le message du dernier commit

Imaginez que vous venez de valider quelques modifications dans votre référentiel Git, mais que vous constatez qu'il y a une faute de frappe dans le message du commit. Vous voulez corriger cette erreur sans modifier les modifications que vous avez effectuées. Comment pouvez-vous le faire?

Pour démontrer comment modifier le message du dernier commit, utilisons le référentiel de `https://github.com/labex-labs/git-playground`. Suivez ces étapes :

1. Clonez le référentiel, accédez au répertoire et configurez l'identité :
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "votre-nom-d'utilisateur"
   git config --global user.email "votre-adresse-email"
   ```
2. Corrigez le message du commit du dernier commit pour qu'il soit "Fix the network bug" :
   ```
   git commit --amend -m "Fix the network bug"
   ```
   Cela ouvrira votre éditeur de texte par défaut où vous pourrez modifier le message du commit. Enregistrez et fermez l'éditeur pour terminer le processus.
3. Vérifiez que le message du commit a été modifié :
   ```
   git log --oneline
   ```

Vous devriez voir le message du commit mis à jour dans le journal :

```
54b830b (HEAD -> master) Fix the network bug
cf80005 Added file1.txt
b00b937 Initial commit
```
