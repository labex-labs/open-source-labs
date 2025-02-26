# React useEventListener Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Cette fonction ajoute un écouteur d'événement pour le type d'événement spécifié sur l'élément donné. Pour utiliser cette fonction, suivez ces étapes :

1. Utilisez le hook `useRef()` pour créer une réf qui contiendra le `handler`.
2. Utilisez le hook `useEffect()` pour mettre à jour la valeur de la réf `savedHandler` chaque fois que le `handler` change.
3. Utilisez le hook `useEffect()` pour ajouter un écouteur d'événement à l'élément donné et le nettoyer lors du démontage.
4. Omettez le dernier argument, `el`, pour utiliser la `Window` par défaut.

Voici le code :

```jsx
const useEventListener = (type, handler, el = window) => {
  const savedHandler = React.useRef(handler);

  React.useEffect(() => {
    savedHandler.current = handler;
  }, [handler]);

  React.useEffect(() => {
    const listener = (e) => savedHandler.current(e);

    el.addEventListener(type, listener);

    return () => {
      el.removeEventListener(type, listener);
    };
  }, [type, el]);
};
```

Et voici un exemple d'utilisation de la fonction `useEventListener()` :

```jsx
const MyApp = () => {
  const [coords, setCoords] = React.useState({ x: 0, y: 0 });

  const updateCoords = React.useCallback(
    ({ clientX, clientY }) => {
      setCoords({ x: clientX, y: clientY });
    },
    [setCoords]
  );

  useEventListener("mousemove", updateCoords);

  return (
    <p>
      Coordonnées de la souris : {coords.x}, {coords.y}
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
