# React useWindowSize Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour suivre les dimensions de la fenêtre du navigateur, les étapes suivantes peuvent être suivies :

1. Utilisez le hook `useState()` pour initialiser une variable d'état `windowSize` qui contiendra les dimensions de la fenêtre. Initialisez-les avec les deux valeurs définies sur `undefined` pour éviter les incohérences entre les rendus serveur et client.

```jsx
const [windowSize, setWindowSize] = React.useState({
  width: undefined,
  height: undefined
});
```

2. Créez une fonction `handleResize()` qui utilise `Window.innerWidth` et `Window.innerHeight` pour mettre à jour la variable d'état. Cette fonction sera appelée chaque fois que l'événement `'resize'` est déclenché.

```jsx
const handleResize = () =>
  setWindowSize({ width: window.innerWidth, height: window.innerHeight });
```

3. Utilisez le hook `useEffect()` pour définir un écouteur approprié pour l'événement `'resize'` au montage et le nettoyer lors du démontage.

```jsx
React.useEffect(() => {
  window.addEventListener("resize", handleResize);

  handleResize();

  return () => {
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

En mettant tout cela ensemble, le hook personnalisé `useWindowSize()` peut être défini comme suit :

```jsx
const useWindowSize = () => {
  const [windowSize, setWindowSize] = React.useState({
    width: undefined,
    height: undefined
  });

  const handleResize = () =>
    setWindowSize({ width: window.innerWidth, height: window.innerHeight });

  React.useEffect(() => {
    window.addEventListener("resize", handleResize);

    handleResize();

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  return windowSize;
};
```

Pour utiliser le hook `useWindowSize()`, appelez-le simplement dans un composant et déstructurez les valeurs `width` et `height` de l'objet renvoyé.

```jsx
const MyApp = () => {
  const { width, height } = useWindowSize();

  return (
    <p>
      Taille de la fenêtre : ({width} x {height})
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
