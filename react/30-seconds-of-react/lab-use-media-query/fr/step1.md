# React useMediaQuery Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Cette fonction vérifie si l'environnement actuel correspond à une requête média donnée et retourne la valeur appropriée.

- Tout d'abord, vérifiez si `Window` et `Window.matchMedia()` existent. Si ce n'est pas le cas (par exemple, dans un environnement SSR ou un navigateur non pris en charge), retournez `whenFalse`.
- Utilisez `Window.matchMedia()` pour correspondre à la `query` donnée. Convertissez sa propriété `matches` en booléen et stockez-la dans une variable d'état, `match`, à l'aide du hook `useState()`.
- Utilisez le hook `useEffect()` pour ajouter un écouteur pour les changements et nettoyer les écouteurs après que le hook ait été détruit.
- Enfin, retournez soit `whenTrue` soit `whenFalse` en fonction de la valeur de `match`.

```jsx
const useMediaQuery = (query, whenTrue, whenFalse) => {
  if (
    typeof window === "undefined" ||
    typeof window.matchMedia === "undefined"
  ) {
    return whenFalse;
  }

  const mediaQuery = window.matchMedia(query);
  const [match, setMatch] = React.useState(!!mediaQuery.matches);

  React.useEffect(() => {
    const handler = () => setMatch(!!mediaQuery.matches);
    mediaQuery.addListener(handler);
    return () => mediaQuery.removeListener(handler);
  }, [mediaQuery]);

  return match ? whenTrue : whenFalse;
};
```

```jsx
const ResponsiveText = () => {
  const text = useMediaQuery(
    "(max-width: 400px)",
    "Less than 400px wide",
    "More than 400px wide"
  );

  return <span>{text}</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ResponsiveText />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
