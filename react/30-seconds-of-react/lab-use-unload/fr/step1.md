# React useUnload Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle (VM). En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

L'événement de fenêtre `beforeunload` peut être géré en utilisant les étapes suivantes :

1. Créez une référence (ref) pour la fonction de rappel (callback), `fn`, en utilisant le hook `useRef()`.
2. Utilisez le hook `useEffect()` et `EventTarget.addEventListener()` pour gérer l'événement `'beforeunload'`, qui est déclenché lorsque l'utilisateur est sur le point de fermer la fenêtre.
3. Utilisez `EventTarget.removeEventListener()` pour effectuer le nettoyage (cleanup) après le démontage du composant.

Voici le code :

```jsx
const useUnload = (fn) => {
  const callbackRef = React.useRef(fn);

  React.useEffect(() => {
    const callback = callbackRef.current;
    window.addEventListener("beforeunload", callback);
    return () => {
      window.removeEventListener("beforeunload", callback);
    };
  }, [callbackRef]);
};

const App = () => {
  useUnload((e) => {
    e.preventDefault();
    const exit = confirm("Are you sure you want to leave?");
    if (exit) window.close();
  });

  return <div>Try closing the window.</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
