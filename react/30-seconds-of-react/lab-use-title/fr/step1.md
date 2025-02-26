# React useTitle Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour définir le titre de la page, vous pouvez utiliser le hook personnalisé `useTitle`. Ce hook utilise `typeof` pour vérifier si `Document` est défini. Si c'est le cas, le hook `useRef()` est utilisé pour stocker le titre original du `Document`. Le hook `useEffect()` est ensuite utilisé pour définir `Document.title` sur la valeur passée lors du montage du composant et pour nettoyer lors du démontage.

```jsx
const useTitle = (title) => {
  const documentDefined = typeof document !== "undefined";
  const originalTitle = React.useRef(documentDefined ? document.title : null);

  React.useEffect(() => {
    if (!documentDefined) return;

    if (document.title !== title) {
      document.title = title;
    }

    return () => {
      document.title = originalTitle.current;
    };
  }, [title]);
};
```

Dans le code d'exemple, le composant `Alert` utilise le hook `useTitle` pour définir le titre sur "Alert". Le composant `MyApp` affiche un bouton qui bascule le composant `Alert`.

```jsx
const Alert = () => {
  useTitle("Alert");

  return (
    <div>
      <p>Alert! Title a changé</p>
    </div>
  );
};

const MyApp = () => {
  const [alertOpen, setAlertOpen] = React.useState(false);

  return (
    <div>
      <button onClick={() => setAlertOpen(!alertOpen)}>
        Basculer l'alerte
      </button>
      {alertOpen && <Alert />}
    </div>
  );
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
