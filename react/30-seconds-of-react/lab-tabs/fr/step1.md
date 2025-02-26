# Tabs

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code dans `script.js` et `style.css`.

Pour afficher un menu à onglets et un composant de vue, suivez ces étapes :

1. Définissez un composant `Tabs`. Utilisez le hook `useState()` pour définir la variable d'état `bindIndex` sur `defaultIndex`.
2. Définissez un composant `TabItem` et filtrez les `children` passés au composant `Tabs` pour supprimer tous les nœuds inutiles sauf `TabItem`. Vous pouvez le faire en identifiant le nom de la fonction.
3. Définissez une fonction appelée `changeTab`. Cette fonction sera exécutée lorsqu'un utilisateur clique sur un `<button>` du menu.
4. `changeTab` exécute la callback passée, `onTabClick`, et met à jour `bindIndex` en fonction de l'élément cliqué.
5. Utilisez `Array.prototype.map()` sur les nœuds collectés pour afficher le menu et la vue des onglets.
6. Utilisez la valeur de `bindIndex` pour déterminer l'onglet actif et appliquer la `className` correcte.

Voici le code CSS pour styliser le menu à onglets et la vue :

```css
.tab-menu > button {
  cursor: pointer;
  padding: 8px 16px;
  border: 0;
  border-bottom: 2px solid transparent;
  background: none;
}

.tab-menu > button.focus {
  border-bottom: 2px solid #007bef;
}

.tab-menu > button:hover {
  border-bottom: 2px solid #007bef;
}

.tab-content {
  display: none;
}

.tab-content.selected {
  display: block;
}
```

Voici le code JavaScript pour implémenter le composant `Tabs` :

```jsx
const TabItem = (props) => <div {...props} />;

const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeTab = (newIndex) => {
    if (typeof onTabClick === "function") onTabClick(newIndex);
    setBindIndex(newIndex);
  };

  const items = children.filter((item) => item.type.name === "TabItem");

  return (
    <div className="wrapper">
      <div className="tab-menu">
        {items.map(({ props: { index, label } }) => (
          <button
            key={`tab-btn-${index}`}
            onClick={() => changeTab(index)}
            className={bindIndex === index ? "focus" : ""}
          >
            {label}
          </button>
        ))}
      </div>
      <div className="tab-view">
        {items.map(({ props }) => (
          <div
            {...props}
            className={`tab-content ${
              bindIndex === props.index ? "selected" : ""
            }`}
            key={`tab-content-${props.index}`}
          />
        ))}
      </div>
    </div>
  );
};
```

Enfin, voici un exemple d'utilisation du composant `Tabs` :

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Tabs defaultIndex={1} onTabClick={console.log}>
    <TabItem label="A" index={1}>
      Lorem ipsum
    </TabItem>
    <TabItem label="B" index={2}>
      Dolor sit amet
    </TabItem>
  </Tabs>
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
