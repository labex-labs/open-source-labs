# React useOnWindowScroll Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Cette fonction exécute une fonction de rappel chaque fois que la fenêtre est défilée. Pour la mettre en œuvre :

1. Utilisez le hook `useRef()` pour créer une variable de référence, `listener`.
2. Utilisez le hook `useEffect()` et `EventTarget.addEventListener()` pour écouter l'événement `'scroll'` de l'objet `Window`, et attribuer la référence du listener à `listener.current`.
3. Utilisez `EventTarget.removeEventListener()` pour supprimer tout écouteur existant lorsque le composant est démonté.

Voici le code :

```jsx
const useOnWindowScroll = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("scroll", listener.current);
    }
    listener.current = () => {
      callback(window.pageYOffset);
    };
    window.addEventListener("scroll", listener.current);
    return () => {
      window.removeEventListener("scroll", listener.current);
    };
  }, [callback]);
};
```

Pour tester la fonction, vous pouvez l'utiliser dans un composant comme ceci :

```jsx
const App = () => {
  useOnWindowScroll((scrollY) => console.log(`scroll Y: ${scrollY}`));
  return <p style={{ height: "300vh" }}>Scroll and check the console</p>;
};

ReactDOM.render(<App />, document.getElementById("root"));
```

Cela affichera la position de défilement verticale de la fenêtre chaque fois qu'elle est défilée.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
