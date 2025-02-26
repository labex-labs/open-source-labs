# Drag Drop

Pour commencer, ouvrez l'éditeur. Vous pouvez voir les fichiers suivants dans votre éditeur.

```txt
├── public
├── src
│   ├── App.js
│   ├── App.css
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

- Veuillez compléter ce défi dans le fichier `App.js`.
- La fonction `onDragStart` est définie. C'est un gestionnaire d'événements pour l'événement dragstart sur une carte de tâche. Elle définit les données de transfert de données sur la propriété name de la tâche, qui sera utilisée pour identifier la tâche lorsqu'elle est déposée.
- La fonction `onDrop` est définie. C'est un gestionnaire d'événements pour l'événement drop sur le tableau de tâches. Elle récupère le nom de la tâche à partir des données de transfert de données, met à jour la catégorie de la tâche dans l'état des tâches en fonction de l'emplacement de dépose (cat), et définit l'état des tâches mis à jour en utilisant setTasks.

## Exemple

Une fois que vous avez terminé le code, exécutez-le avec la commande suivante :

```bash
npm start
```

Le résultat final est le suivant :

![Drag and drop demo](../assets/finished.gif)
