# React useSearchParam Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour suivre le paramètre de recherche de l'emplacement du navigateur, utilisez les étapes suivantes :

1. Créez une fonction de rappel en utilisant le hook `useCallback()`. La fonction de rappel devrait utiliser le constructeur `URLSearchParams` pour obtenir la valeur actuelle du paramètre souhaité.

```jsx
const getValue = React.useCallback(
  () => new URLSearchParams(window.location.search).get(param),
  [param]
);
```

2. Créez une variable d'état qui stocke la valeur actuelle du paramètre en utilisant le hook `useState()`.

```jsx
const [value, setValue] = React.useState(getValue);
```

3. Configurez des écouteurs d'événements appropriés pour mettre à jour la variable d'état lors du montage et les nettoyer lors du démontage en utilisant le hook `useEffect()`.

```jsx
React.useEffect(() => {
  const onChange = () => {
    setValue(getValue());
  };

  window.addEventListener("popstate", onChange);
  window.addEventListener("pushstate", onChange);
  window.addEventListener("replacestate", onChange);

  return () => {
    window.removeEventListener("popstate", onChange);
    window.removeEventListener("pushstate", onChange);
    window.removeEventListener("replacestate", onChange);
  };
}, []);
```

Voici un exemple de manière d'utiliser ce hook personnalisé dans un composant :

```jsx
const MyApp = () => {
  const post = useSearchParam("post");

  return (
    <>
      <p>Valeur du paramètre post : {post || "null"}</p>
      <button
        onClick={() =>
          history.pushState({}, "", location.pathname + "?post=42")
        }
      >
        Voir le post 42
      </button>
      <button onClick={() => history.pushState({}, "", location.pathname)}>
        Sortir
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Cet exemple crée un composant `MyApp` qui utilise le hook personnalisé `useSearchParam` pour suivre la valeur du paramètre `post` dans la recherche de l'emplacement. La valeur de `post` est affichée dans une balise de paragraphe. Deux boutons sont également inclus pour démontrer comment changer la valeur du paramètre de recherche d'emplacement.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
