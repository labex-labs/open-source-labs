# React useDefault Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Voici le code :

```jsx
const useDefault = (defaultState, initialState) => {
  const [value, setValue] = React.useState(initialState);
  const isEmpty = value === undefined || value === null;
  return [isEmpty ? defaultState : value, setValue];
};
```

```jsx
const UserCard = () => {
  const [user, setUser] = useDefault({ name: "Adam" }, { name: "John" });

  return (
    <>
      <div>User: {user.name}</div>
      <input onChange={(e) => setUser({ name: e.target.value })} />
      <button onClick={() => setUser(null)}>Clear</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<UserCard />);
```

Pour créer une valeur avec état avec une valeur de repli par défaut, utilisez le hook `useState()` en React. Vérifiez si la valeur initiale est soit `null` soit `undefined`. Si c'est le cas, renvoyez le `defaultState` à la place, sinon renvoyez l'état `value` réel et la fonction `setValue`. Le code ci-dessus montre comment implémenter cette fonctionnalité dans un hook personnalisé appelé `useDefault`.

Dans l'exemple fourni, `useDefault` est utilisé pour créer un état `user` avec une valeur par défaut de `{ name: 'Adam' }`. L'état initial est défini sur `{ name: 'John' }`. Dans le composant `UserCard`, `user` est affiché avec un champ de saisie pour mettre à jour son nom. Un bouton de nettoyage est également fourni pour réinitialiser l'état à `null`. Enfin, le composant est rendu à l'aide de `ReactDOM.createRoot()`.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
