# React useLocalStorage Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Cette fonction crée une valeur qui est enregistrée dans `localStorage` et une fonction pour la modifier. Voici comment elle fonctionne :

1. Pour créer la valeur, utilisez le hook `useState()` avec une fonction pour l'initialiser de manière paresseuse.
2. Pour récupérer la valeur enregistrée dans `localStorage`, utilisez un bloc `try...catch` et `Storage.getItem()`. Si aucune valeur n'est enregistrée, utilisez `Storage.setItem()` pour enregistrer la `defaultValue` et l'utiliser comme état initial. Si une erreur se produit, utilisez `defaultValue`.
3. Définissez une fonction qui met à jour la variable d'état avec la valeur passée et utilise `Storage.setItem()` pour l'enregistrer.

Voici le code :

```jsx
const useLocalStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.localStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.localStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

Vous pouvez utiliser cette fonction dans votre application comme ceci :

```jsx
const MyApp = () => {
  const [name, setName] = useLocalStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
