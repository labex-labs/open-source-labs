# React useOnGlobalEvent Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Cette fonction exécute une fonction de rappel chaque fois qu'un événement se produit sur l'objet global. Pour implémenter cette fonction :

1. Utilisez le hook `useRef()` pour créer une variable, `listener`, qui contiendra la référence du listener.
2. Utilisez le hook `useRef()` pour créer une variable qui contiendra les valeurs précédentes des arguments `type` et `options`.
3. Utilisez le hook `useEffect()` et `EventTarget.addEventListener()` pour écouter l'événement `type` donné sur l'objet global `Window`.
4. Utilisez `EventTarget.removeEventListener()` pour supprimer tout listener existant et nettoyer lorsque le composant est démonté.

```jsx
const useOnGlobalEvent = (type, callback, options) => {
  const listener = React.useRef(null);
  const previousProps = React.useRef({ type, options });

  React.useEffect(() => {
    const { type: previousType, options: previousOptions } =
      previousProps.current;

    if (listener.current) {
      window.removeEventListener(
        previousType,
        listener.current,
        previousOptions
      );
    }

    listener.current = callback;
    window.addEventListener(type, callback, options);
    previousProps.current = { type, options };

    return () => {
      window.removeEventListener(type, listener.current, options);
    };
  }, [callback, type, options]);
};
```

Voici un exemple d'utilisation de cette fonction :

```jsx
const App = () => {
  useOnGlobalEvent("mousemove", (e) => {
    console.log(`(${e.x}, ${e.y})`);
  });

  return <p>Move your mouse around</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
