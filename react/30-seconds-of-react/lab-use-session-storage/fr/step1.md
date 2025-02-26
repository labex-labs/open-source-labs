# React useSessionStorage Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour créer une valeur d'état qui est persistée dans `sessionStorage`, et une fonction pour la mettre à jour, suivez ces étapes :

1. Utilisez le hook `useState()` avec une fonction pour initialiser sa valeur de manière paresseuse.
2. Utilisez un bloc `try...catch` et `Storage.getItem()` pour essayer de récupérer la valeur de `Window.sessionStorage`. Si aucune valeur n'est trouvée, utilisez `Storage.setItem()` pour stocker la `defaultValue` et l'utiliser comme état initial. Si une erreur se produit, utilisez `defaultValue` comme état initial.
3. Définissez une fonction qui mettra à jour la variable d'état avec la valeur passée et utilisez `Storage.setItem()` pour la stocker.

Voici une implémentation d'exemple :

```jsx
const useSessionStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.sessionStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

Vous pouvez utiliser ce hook dans votre application comme ceci :

```jsx
const MyApp = () => {
  const [name, setName] = useSessionStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
