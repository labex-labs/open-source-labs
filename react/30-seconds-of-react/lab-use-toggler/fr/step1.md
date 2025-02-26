# React useToggler Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour créer une variable d'état booléenne qui peut être basculée entre ses deux états, suivez ces étapes :

1. Utilisez le hook `useState()` pour créer la variable d'état `value` et son mutateur.
2. Créez une fonction qui bascule la valeur de la variable d'état `value` et mémoisez-la, en utilisant le hook `useCallback()`.
3. Retournez la variable d'état `value` et la fonction de basculement mémoisée.

Voici une implémentation d'exemple :

```jsx
const useToggler = (initialState) => {
  const [value, setValue] = React.useState(initialState);

  const toggleValue = React.useCallback(() => setValue((prev) => !prev), []);

  return [value, toggleValue];
};
```

Vous pouvez ensuite utiliser ce hook dans vos composants, comme ceci :

```jsx
const Switch = () => {
  const [val, toggleVal] = useToggler(false);
  return <button onClick={toggleVal}>{val ? "ON" : "OFF"}</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Switch />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
