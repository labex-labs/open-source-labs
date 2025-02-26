# React useHover Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce code crée un hook personnalisé qui gère le survol d'un composant encapsulé.

Pour utiliser le hook :

- Utilisez `useState()` pour créer une variable qui stocke l'état de survol.
- Utilisez `useCallback()` pour mémoïser deux fonctions de gestionnaires qui mettent à jour l'état.
- Utilisez `useCallback()` pour créer une réf de rappel et créer ou mettre à jour les écouteurs pour les événements `'mouseover'` et `'mouseout'`.
- Utilisez `useRef()` pour suivre le dernier nœud passé à `callbackRef` afin de pouvoir supprimer ses écouteurs.

```jsx
const useHover = () => {
  const [isHovering, setIsHovering] = React.useState(false);
  const handleMouseOver = React.useCallback(() => setIsHovering(true), []);
  const handleMouseOut = React.useCallback(() => setIsHovering(false), []);
  const nodeRef = React.useRef();
  const callbackRef = React.useCallback(
    (node) => {
      if (nodeRef.current) {
        nodeRef.current.removeEventListener("mouseover", handleMouseOver);
        nodeRef.current.removeEventListener("mouseout", handleMouseOut);
      }
      nodeRef.current = node;
      if (nodeRef.current) {
        nodeRef.current.addEventListener("mouseover", handleMouseOver);
        nodeRef.current.addEventListener("mouseout", handleMouseOut);
      }
    },
    [handleMouseOver, handleMouseOut]
  );

  return [callbackRef, isHovering];
};
```

Voici un exemple d'utilisation du hook :

```jsx
const MyApp = () => {
  const [hoverRef, isHovering] = useHover();
  return <div ref={hoverRef}>{isHovering ? "Survol" : "Pas en survol"}</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
