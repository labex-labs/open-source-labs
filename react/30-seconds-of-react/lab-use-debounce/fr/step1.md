# React useDebounce Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour gérer le rebondissement d'une valeur donnée, vous pouvez créer un hook personnalisé qui prend une `valeur` et un `délai`. Utilisez le hook `useState()` pour stocker la valeur rebondie, et le hook `useEffect()` pour mettre à jour la valeur rebondie chaque fois que `valeur` est mise à jour. Pour retarder l'appel du setter de la variable d'état précédente de `délai` ms, utilisez `setTimeout()`. Pour nettoyer lors de la désinstallation du composant, utilisez `clearTimeout()`. Cela est particulièrement utile lorsqu'il s'agit d'entrée utilisateur.

Voici une implémentation exemple du hook `useDebounce()` :

```jsx
const useDebounce = (value, delay) => {
  const [debouncedValue, setDebouncedValue] = React.useState(value);

  React.useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
};
```

Vous pouvez utiliser le hook `useDebounce()` dans un composant comme ceci :

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = useDebounce(value, 500);

  return (
    <div>
      <p>
        Actuel : {value} - Rebondi : {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Incrémenter</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
