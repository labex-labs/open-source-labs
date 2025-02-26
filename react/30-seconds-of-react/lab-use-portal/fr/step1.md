# React usePortal Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour créer un portail qui rend les enfants en dehors du composant parent, suivez ces étapes :

1. Utilisez le hook `useState()` pour créer une variable d'état qui contient les fonctions `render()` et `remove()` pour le portail.
2. Utilisez `ReactDOM.createPortal()` et `ReactDOM.unmountComponentAtNode()` pour créer un portail et une fonction pour le supprimer. Utilisez le hook `useCallback()` pour encapsuler et mémoïser ces fonctions sous forme de `createPortal()`.
3. Utilisez le hook `useEffect()` pour appeler `createPortal()` et mettre à jour la variable d'état chaque fois que la valeur de `el` change.
4. Enfin, renvoyez la fonction `render()` de la variable d'état.

Voici une implémentation d'exemple :

```jsx
const usePortal = (el) => {
  const [portal, setPortal] = React.useState({
    render: () => null,
    remove: () => null
  });

  const createPortal = React.useCallback((el) => {
    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
    const remove = () => ReactDOM.unmountComponentAtNode(el);
    return { render: Portal, remove };
  }, []);

  React.useEffect(() => {
    if (el) portal.remove();
    const newPortal = createPortal(el);
    setPortal(newPortal);
    return () => newPortal.remove(el);
  }, [el]);

  return portal.render;
};
```

Pour utiliser ce hook, créez un composant qui appelle `usePortal()` avec l'élément DOM souhaité en tant qu'argument. Ce composant peut ensuite utiliser la fonction `render()` renvoyée pour rendre du contenu dans le portail :

```jsx
const App = () => {
  const Portal = usePortal(document.querySelector("title"));

  return (
    <p>
      Bonjour le monde!
      <Portal>Titre portalisé</Portal>
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
