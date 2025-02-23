# Ajoutez un modèle de message de commit

Sans un modèle de message de commit, les développeurs peuvent être tentés d'écrire des messages de commit vagues ou non informatifs, tels que "correction de bogue" ou "mise à jour du code". Cela rend difficile pour les autres de comprendre le but de la modification et peut entraîner la confusion ou des erreurs plus tard. En configurant un modèle de message de commit, on encourage les développeurs à fournir des messages de commit plus détaillés et informatifs, ce qui peut améliorer la collaboration et la productivité.

Pour ce laboratoire, utilisons le référentiel de `https://github.com/labex-labs/git-playground`. Suivez ces étapes pour configurer un modèle de message de commit pour ce référentiel :

1. Clonez le référentiel sur votre machine locale en utilisant la commande `git clone https://github.com/labex-labs/git-playground`.
2. Accédez au répertoire du référentiel en utilisant la commande `cd git-playground` et configurez votre compte GitHub en utilisant les commandes `git config --global user.name "votre-nom-d'utilisateur"` et `git config --global user.email "votre-email"`.
3. Créez un nouveau fichier nommé `commit-template` dans le répertoire du référentiel en utilisant la commande `vim commit-template`.
4. Ouvrez le fichier `commit-template` dans un éditeur de texte et ajoutez les lignes suivantes :

```shell
# <type>: <sujet>

# <corps>

# <pied de page>

#Cela crée un modèle avec trois sections, où "<type>" indique le type de soumission, tel que "feat" ou "fix", "<sujet>" est un résumé bref décrivant le contenu de la soumission, "<corps>" est une description plus détaillée et "<pied de page>" peut contenir d'autres métadonnées, telles que le numéro de problème associé ou d'autres commentaires.
```

5. Appuyez sur <kbd>Esc</kbd> et entrez la commande <kbd>:wq</kbd>, puis appuyez sur <kbd>Entrée</kbd> pour enregistrer vos modifications et quitter l'éditeur de fichier `commit-template`.
6. Utilisez la commande `git add commit-template` pour ajouter les fichiers `commit-template` à la zone de préparation.
7. Utilisez la commande `git config commit.template commit-template` pour définir le fichier `commit-template` comme modèle de message de commit pour le référentiel.
8. Utilisez la commande `git commit` pour ouvrir l'éditeur de message de commit et remarquez que l'éditeur de message de commit contient désormais le modèle de message de commit que vous avez créé à l'étape 4.
9. Appuyez sur <kbd>Esc</kbd> et entrez la commande <kbd>:q</kbd>, puis appuyez sur <kbd>Entrée</kbd> pour quitter l'éditeur de message de commit.
