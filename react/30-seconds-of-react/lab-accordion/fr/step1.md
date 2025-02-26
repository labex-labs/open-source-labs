# Menu accordéon rétractable

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour afficher un menu accordéon avec plusieurs éléments de contenu rétractables, vous pouvez suivre ces étapes :

1. Définissez un composant `AccordionItem` qui rend un `<button>` et met à jour le composant tout en informant son parent via la callback `handleClick`.
2. Utilisez la propriété `isCollapsed` dans `AccordionItem` pour déterminer son apparence et définir sa `className`.
3. Définissez un composant `Accordion` et utilisez le hook `useState()` pour initialiser la valeur de la variable d'état `bindIndex` à `defaultIndex`.
4. Filtrez `children` pour supprimer les nœuds inutiles, sauf `AccordionItem`, en identifiant le nom de la fonction.
5. Utilisez `Array.prototype.map()` sur les nœuds collectés pour afficher les éléments rétractables individuels.
6. Définissez `changeItem`, qui sera exécutée lors du clic sur le `<button>` d'un `AccordionItem`.
7. `changeItem` exécute la callback passée, `onItemClick`, et met à jour `bindIndex` en fonction de l'élément cliqué.

Voici le code :

```css
.accordion-item.collapsed {
  display: none;
}

.accordion-item.expanded {
  display: block;
}

.accordion-button {
  display: block;
  width: 100%;
}
```

```jsx
const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
  return (
    <>
      <button className="accordion-button" onClick={handleClick}>
        {label}
      </button>
      <div
        className={`accordion-item ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};

const Accordion = ({ defaultIndex, onItemClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeItem = (itemIndex) => {
    if (typeof onItemClick === "function") onItemClick(itemIndex);
    if (itemIndex !== bindIndex) setBindIndex(itemIndex);
  };

  const items = children.filter((item) => item.type.name === "AccordionItem");

  return (
    <>
      {items.map(({ props }) => (
        <AccordionItem
          isCollapsed={bindIndex !== props.index}
          label={props.label}
          handleClick={() => changeItem(props.index)}
          children={props.children}
        />
      ))}
    </>
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Accordion defaultIndex="1" onItemClick={console.log}>
    <AccordionItem label="A" index="1">
      Lorem ipsum
    </AccordionItem>
    <AccordionItem label="B" index="2">
      Dolor sit amet
    </AccordionItem>
  </Accordion>
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
