# Créer un commit vide

Vous devez créer un commit vide dans votre référentiel Git. Cela peut être utile dans plusieurs scénarios, tels que :

- Décencher un processus de génération
- Créer un commit de point d'arrêt
- Marquer un point spécifique dans l'historique du référentiel

Pour ce laboratoire, utilisons le référentiel de `https://github.com/labex-labs/git-playground` :

1. Clonez le référentiel sur votre machine locale en utilisant la commande `git clone https://github.com/labex-labs/git-playground`.
2. Accédez au répertoire du référentiel en utilisant la commande `cd git-playground` et configurez votre compte github dans l'environnement en utilisant les commandes `git config --global user.name "votre-nom-d'utilisateur"` et `git config --global user.email "votre-email"`.
3. Utilisez la commande `git commit --allow-empty -m "Commit vide"` pour créer un commit vide avec le message "Commit vide".
4. Vérifiez que le commit vide a été créé en utilisant la commande `git log --name-status HEAD^..HEAD`.

Voici où vous exécutez `git log --name-status HEAD^..HEAD` et le résultat :

![Résultat du commit vide de git log](../assets/challenge-create-empty-commit-step1-1.png)
