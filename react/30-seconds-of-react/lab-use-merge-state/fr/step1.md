# React useMergeState Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour créer une valeur avec état et une fonction pour la mettre à jour en fusionnant le nouvel état fourni, utilisez le hook `useState()` pour créer une variable d'état et l'initialiser avec `initialState`. Créez une fonction qui mettra à jour la variable d'état en fusionnant le nouvel état fourni avec l'état existant. Si le nouvel état est une fonction, appelez-la avec l'état précédent comme argument et utilisez le résultat. Si aucun argument n'est fourni, la variable d'état sera initialisée avec un objet vide (`{}`). Le code suivant montre comment implémenter cela en utilisant le hook personnalisé `useMergeState` :

```jsx
const useMergeState = (initialState = {}) => {
  const [value, setValue] = React.useState(initialState);

  const mergeState = (newState) => {
    if (typeof newState === "function") {
      newState = newState(value);
    }
    setValue({ ...value, ...newState });
  };

  return [value, mergeState];
};
```

Voici un exemple d'utilisation du hook `useMergeState` dans un composant nommé `MyApp` :

```jsx
const MyApp = () => {
  const [data, setData] = useMergeState({ name: "John", age: 20 });

  return (
    <>
      <input
        value={data.name}
        onChange={(e) => setData({ name: e.target.value })}
      />
      <button onClick={() => setData(({ age }) => ({ age: age - 1 }))}>
        -
      </button>
      {data.age}
      <button onClick={() => setData(({ age }) => ({ age: age + 1 }))}>
        +
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
