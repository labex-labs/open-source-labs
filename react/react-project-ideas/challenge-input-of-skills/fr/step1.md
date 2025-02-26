# Entrée de compétences

Pour commencer, ouvrez l'éditeur. Vous pouvez voir les fichiers suivants à partir de votre éditeur.

```txt
├── public
├── src
│   ├── components
│   │   └── TagInput.js
│   ├── App.css
│   ├── App.js
│   ├── index.css
│   └── index.js
├── package-lock.json
└── package.json
```

## Exigences

- Pour installer les dépendances du projet, utilisez la commande suivante :

  ```bash
  npm i
  ```

- Veuillez compléter ce défi dans le fichier `src/component/TagInput.js`.
- La fonction `handleAddTag` est appelée lorsqu'une touche est pressée dans le champ d'entrée. Si la touche n'est pas la touche Entrée, la fonction retourne immédiatement et ne fait rien. Sinon, elle vérifie la valeur d'entrée et l'ajoute à l'état des étiquettes si elle n'est pas vide et n'a pas déjà été ajoutée. Ensuite, elle efface le champ d'entrée.
- La fonction `onDeleteTag` est appelée lorsqu'une étiquette est cliquée. Elle filtre l'état des étiquettes pour supprimer l'étiquette cliquée et met à jour l'état avec les étiquettes filtrées.

## Exemple

Une fois que vous avez terminé le code, exécutez-le avec la commande suivante :

```bash
npm start
```

Le résultat final est le suivant :

![Tag input functionality demo](../assets/finished.gif)
