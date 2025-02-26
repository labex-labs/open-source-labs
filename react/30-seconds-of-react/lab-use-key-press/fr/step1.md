# React useKeyPress Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Cette fonction écoute les changements de l'état appuyé d'une touche donnée. Pour l'utiliser :

- Appelez `useKeyPress()` avec la touche cible en argument.
- `useKeyPress()` renvoie une valeur booléenne qui indique si la touche est enfoncée actuellement.
- La fonction utilise le hook `useState()` pour créer une variable d'état qui stocke l'état appuyé de la touche donnée.
- Elle définit deux fonctions de gestionnaires qui mettent à jour la variable d'état lors de la pression ou du relâchement de la touche en conséquence.
- Le hook `useEffect()` et `EventTarget.addEventListener()` sont utilisés pour gérer les événements `'keydown'` et `'keyup'`.
- Enfin, `EventTarget.removeEventListener()` est utilisé pour effectuer le nettoyage après que le composant soit démonté.

```jsx
const useKeyPress = (targetKey) => {
  const [isKeyPressed, setKeyPressed] = React.useState(false);

  const handleKeyDown = ({ key }) => {
    if (key === targetKey) setKeyPressed(true);
  };

  const handleKeyUp = ({ key }) => {
    if (key === targetKey) setKeyPressed(false);
  };

  React.useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("keyup", handleKeyUp);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("keyup", handleKeyUp);
    };
  }, [targetKey]);

  return isKeyPressed;
};
```

Voici un exemple d'utilisation de `useKeyPress()` dans un composant React :

```jsx
const MyApp = () => {
  const isWKeyPressed = useKeyPress("w");

  return <p>The "w" key is {!isWKeyPressed ? "not " : ""}pressed!</p>;
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
