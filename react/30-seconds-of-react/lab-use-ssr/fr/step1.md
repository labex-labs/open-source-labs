# React useSSR Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour vérifier si le code est exécuté dans un navigateur ou sur un serveur, créez un hook personnalisé qui utilise `typeof`, `Window`, `Window.document` et `Document.createElement()` pour déterminer si le DOM est disponible. Utilisez le hook `useState()` pour définir la variable d'état `inBrowser` et le hook `useEffect()` pour la mettre à jour et la nettoyer à la fin. Utilisez le hook `useMemo()` pour mémoïser les valeurs de retour du hook personnalisé.

Voici le code :

```jsx
const isDOMavailable = !!(
  typeof window !== "undefined" &&
  window.document &&
  window.document.createElement
);

const useSSR = () => {
  const [inBrowser, setInBrowser] = React.useState(isDOMavailable);

  React.useEffect(() => {
    setInBrowser(isDOMavailable);
    return () => {
      setInBrowser(false);
    };
  }, []);

  const useSSRObject = React.useMemo(
    () => ({
      isBrowser: inBrowser,
      isServer: !inBrowser,
      canUseWorkers: typeof Worker !== "undefined",
      canUseEventListeners: inBrowser && !!window.addEventListener,
      canUseViewport: inBrowser && !!window.screen
    }),
    [inBrowser]
  );

  return useSSRObject;
};

const SSRChecker = (props) => {
  const { isBrowser, isServer } = useSSR();

  return (
    <p>{isBrowser ? "Exécuté dans le navigateur" : "Exécuté sur le serveur"}</p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<SSRChecker />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
