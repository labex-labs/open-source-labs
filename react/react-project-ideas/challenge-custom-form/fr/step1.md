# Formulaire personnalisé

Pour commencer, ouvrez l'éditeur. Vous pouvez voir les fichiers suivants dans votre éditeur.

```txt
├── public
├── src
│   ├── components
│   │   └── CustomForm
│   │       ├── CustomForm.css
│   │       └── CustomForm.js
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

- Veuillez compléter ce défi dans le fichier `App.js`.
- Utilisez le hook `useRef` pour créer deux objets de réf, `usernameRef` et `passwordRef`. Ces réf seront utilisées pour accéder aux valeurs des champs de saisie.
- Fonction `handleLogin` : Cette fonction est appelée lorsque le bouton "Connexion" est cliqué. Elle enregistre les valeurs des champs de saisie du nom d'utilisateur et du mot de passe dans la console et affiche une alerte avec le nom d'utilisateur et le mot de passe entrés.
- Fonction `handleRegister` : Cette fonction est appelée lorsque le bouton "Inscription" est cliqué. Elle enregistre les valeurs des champs de saisie du nom d'utilisateur et du mot de passe dans la console.

## Exemple

Une fois que vous avez terminé le code, exécutez-le avec la commande suivante :

```bash
npm start
```

Le résultat final est le suivant :

![Custom Form Final Result](../assets/finished.gif)
