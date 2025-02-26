# React useMap Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

- Le hook `useMap()` crée un objet `Map` avec état et un ensemble de fonctions pour le manipuler à l'aide des hooks React.
- Le hook `useState()` initialise l'état `Map` avec la `initialValue`.
- Le hook `useMemo()` crée un ensemble d'actions non mutantes qui manipulent la variable d'état `map` en utilisant le mutateur d'état pour créer une nouvelle `Map` à chaque fois.
- Le hook `useMap()` renvoie un tableau contenant la variable d'état `map` et les `actions` créées.
- Le composant `MyApp` utilise le hook `useMap()` pour initialiser l'objet `Map` avec état et fournit des boutons pour ajouter, réinitialiser et supprimer des éléments du `Map`.
- La fonction `JSON.stringify()` formate l'objet `Map` en une chaîne JSON lisible.

```jsx
const useMap = (initialValue) => {
  const [map, setMap] = React.useState(new Map(initialValue));

  const actions = React.useMemo(
    () => ({
      set: (key, value) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.set(key, value);
          return nextMap;
        }),
      remove: (key) =>
        setMap((prevMap) => {
          const nextMap = new Map(prevMap);
          nextMap.delete(key);
          return nextMap;
        }),
      clear: () => setMap(new Map())
    }),
    [setMap]
  );

  return [map, actions];
};

const MyApp = () => {
  const [map, { set, remove, clear }] = useMap([["apples", 10]]);

  const handleAdd = () => set(Date.now(), new Date().toJSON());
  const handleReset = () => clear();
  const handleRemove = () => remove("apples");

  return (
    <div>
      <button onClick={handleAdd}>Ajouter</button>
      <button onClick={handleReset}>Réinitialiser</button>
      <button onClick={handleRemove} disabled={!map.has("apples")}>
        Supprimer les pommes
      </button>
      <pre>{JSON.stringify(Object.fromEntries(map), null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
