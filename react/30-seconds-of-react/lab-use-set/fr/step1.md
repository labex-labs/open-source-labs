# React useSet Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Cette fonction crée un objet `Set` avec état et un ensemble de fonctions qui peuvent manipuler l'état.

Pour utiliser cette fonction :

- Appelez `useState()` et le constructeur `Set` pour créer un nouveau `Set` à partir de la `initialValue`.
- Utilisez `useMemo()` pour créer un ensemble de fonctions non mutantes qui peuvent manipuler la variable d'état `set`. Utilisez le mutateur d'état pour créer un nouveau `Set` à chaque fois.
- Retournez à la fois la variable d'état `set` et les `actions` créées.

Voici une implémentation exemple de cette fonction :

```jsx
const useSet = (initialValue) => {
  const [set, setSet] = React.useState(new Set(initialValue));

  const actions = React.useMemo(
    () => ({
      add: (item) => setSet((prevSet) => new Set([...prevSet, item])),
      remove: (item) =>
        setSet((prevSet) => new Set([...prevSet].filter((i) => i !== item))),
      clear: () => setSet(new Set())
    }),
    [setSet]
  );

  return [set, actions];
};
```

Voici un exemple d'utilisation de cette fonction :

```jsx
const MyApp = () => {
  const [set, { add, remove, clear }] = useSet(new Set(["apples"]));

  return (
    <div>
      <button onClick={() => add(String(Date.now()))}>Ajouter</button>
      <button onClick={() => clear()}>Réinitialiser</button>
      <button onClick={() => remove("apples")} disabled={!set.has("apples")}>
        Supprimer les pommes
      </button>
      <pre>{JSON.stringify([...set], null, 2)}</pre>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
