# React useUpdate Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour forcer un composant à se re-rendre lorsqu'il est appelé, utilisez le hook `useReducer()` pour créer un nouvel objet à chaque mise à jour et renvoyer sa fonction de dispatch. Voici une implémentation de l'exemple de la fonction `useUpdate()` :

```jsx
const useUpdate = () => {
  const [, update] = React.useReducer(() => ({}));
  return update;
};
```

Vous pouvez ensuite utiliser `useUpdate()` dans votre composant pour déclencher un re-rendu si nécessaire :

```jsx
const MyApp = () => {
  const update = useUpdate();

  return (
    <>
      <div>Heure : {Date.now()}</div>
      <button onClick={update}>Mettre à jour</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
