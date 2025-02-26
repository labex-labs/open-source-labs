# Hook React useOnWindowResize

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce code exécute une fonction de rappel chaque fois que la fenêtre est redimensionnée. Pour la mettre en œuvre, vous devriez suivre ces étapes :

1. Créez une variable appelée `listener` à l'aide du hook `useRef()`. Cette variable stockera la référence au listener.

2. Utilisez le hook `useEffect()` et `EventTarget.addEventListener()` pour écouter l'événement `'resize'` de l'objet global `Window`. Lorsque l'événement est déclenché, appelez la fonction `callback`.

3. Nettoyez en supprimant tous les listeners existants avec `EventTarget.removeEventListener()` lorsque le composant est démonté.

Voici le code :

```jsx
const useOnWindowResize = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("resize", listener.current);
    }
    listener.current = callback;
    window.addEventListener("resize", callback);
    return () => {
      window.removeEventListener("resize", callback);
    };
  }, [callback]);
};

const App = () => {
  useOnWindowResize(() =>
    console.log(
      `Taille de la fenêtre : (${window.innerWidth}, ${window.innerHeight})`
    )
  );
  return <p>Redimensionnez la fenêtre et vérifiez la console.</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
