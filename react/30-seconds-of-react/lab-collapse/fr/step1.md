# Contenu rétractable

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Cette fonction affiche un composant rétractable avec un bouton qui bascule la visibilité de son contenu. Voici comment l'utiliser :

1. Utilisez le hook `useState()` pour créer la variable d'état `isCollapsed`, qui représente si le contenu est actuellement rétracté ou déplié. Initialisez-la à `collapsed`.
2. Utilisez l'élément `<button>` pour basculer l'état `isCollapsed` et afficher/cacher le contenu passé via la propriété `children`.
3. Utilisez `isCollapsed` pour appliquer la classe CSS appropriée au conteneur de contenu, soit `collapsed` soit `expanded`, qui détermine son apparence.
4. Mettez à jour l'attribut `aria-expanded` du conteneur de contenu en fonction de l'état `isCollapsed`, pour rendre le composant accessible aux utilisateurs handicapés.

Voici le code CSS nécessaire pour ce composant :

```css
.collapse-button {
  display: block;
  width: 100%;
}

.collapse-content.collapsed {
  display: none;
}

.collapse-content.expanded {
  display: block;
}
```

Et voici le code JavaScript :

```jsx
const Collapse = ({ collapsed, children }) => {
  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);

  return (
    <>
      <button
        className="collapse-button"
        onClick={() => setIsCollapsed(!isCollapsed)}
      >
        {isCollapsed ? "Afficher" : "Cacher"} le contenu
      </button>
      <div
        className={`collapse-content ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};
```

Pour utiliser ce composant, appelez-le simplement avec le contenu que vous voulez rétracter :

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Collapse>
    <h1>Ceci est un rétractable</h1>
    <p>Bonjour le monde!</p>
  </Collapse>
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
