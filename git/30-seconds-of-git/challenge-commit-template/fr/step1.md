# Ajoutez un modèle de message de commit

Sans un modèle de message de commit, les développeurs peuvent être tentés d'écrire des messages de commit vagues ou non informatifs, tels que "correction de bogue" ou "mise à jour du code". Cela rend difficile pour les autres de comprendre le but de la modification et peut entraîner de la confusion ou des erreurs plus tard. En configurant un modèle de message de commit, on encourage les développeurs à fournir des messages de commit plus détaillés et informatifs, ce qui peut améliorer la collaboration et la productivité.

## Tâches

Pour ce défi, utilisons le référentiel de `https://github.com/labex-labs/git-playground`.

1. Accédez au répertoire du référentiel et configurez votre identité GitHub.
2. Créez un nouveau fichier appelé `commit-template` dans le répertoire actuel du référentiel.
3. Ouvrez le fichier `commit-template` dans un éditeur de texte et ajoutez les lignes suivantes :

```shell
# <type> : <sujet>

# <corps>

# <pied de page>

# Cela crée un modèle avec trois sections :
# "<type>" indique le type de soumission, tel que "feat" ou "fix"
# "<sujet>" est un résumé court décrivant le contenu de la soumission
# "<corps>" est une description plus détaillée
# "<pied de page>" peut contenir d'autres métadonnées, telles que le numéro de problème associé ou d'autres commentaires.
```

4. Appuyez sur <kbd>Esc</kbd> puis entrez la commande <kbd>:wq</kbd>, puis appuyez sur <kbd>Entrée</kbd> pour enregistrer vos modifications et quitter l'éditeur de fichier `commit-template`.
5. Ajoutez les fichiers `commit-template` à la zone de préparation.
6. Définissez le fichier `commit-template` comme modèle de message de commit pour le référentiel.
7. Ouvrez l'éditeur de message de commit et remarquez que l'éditeur de message de commit contient désormais le modèle de message de commit que vous avez créé à l'étape 3.
8. Appuyez sur <kbd>Esc</kbd> puis entrez la commande <kbd>:q</kbd>, puis appuyez sur <kbd>Entrée</kbd> pour quitter l'éditeur de message de commit.
