# React useGetSet Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce bout de code définit un hook personnalisé React appelé `useGetSet` qui crée une valeur avec état et renvoie une paire de fonctions pour obtenir et définir sa valeur. Le composant `Counter` utilise ce hook pour implémenter une incrémentation retardée d'un compte affiché dans un bouton.

```jsx
const useGetSet = (initialState) => {
  const stateRef = React.useRef(initialState);
  const [, update] = React.useReducer(() => ({}), {});

  const getState = React.useCallback(() => stateRef.current, []);
  const setState = React.useCallback((newState) => {
    stateRef.current = newState;
    update();
  }, []);

  return [getState, setState];
};

const Counter = () => {
  const [getCount, setCount] = useGetSet(0);
  const onClick = React.useCallback(() => {
    setTimeout(() => {
      setCount(getCount() + 1);
    }, 1000);
  }, [getCount, setCount]);

  return <button onClick={onClick}>Count: {getCount()}</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
