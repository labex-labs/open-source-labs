# React useError Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle (VM). En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce code crée un dispatcher d'erreurs. Il utilise trois hooks React pour gérer l'état des erreurs et les envoyer à l'interface utilisateur.

Voici comment le code fonctionne :

1. Le hook `useState()` crée une variable d'état appelée `error` qui contient l'objet d'erreur. Il prend une valeur initiale de `err`, qui est passée en argument au hook.

2. Le hook `useEffect()` est utilisé pour « lancer » l'erreur chaque fois qu'elle est évaluée à `true`. Ce hook prend une fonction et un tableau de dépendances en arguments. Dans ce cas, la fonction vérifie si la variable d'état `error` est évaluée à `true` (c'est-à-dire non nulle, non indéfinie, différente de 0, de `false` ou d'une chaîne vide), et la lance si c'est le cas. Le tableau de dépendances est `[error]`, ce qui signifie que l'effet sera réexécuté chaque fois que la variable `error` change.

3. Le hook `useCallback()` est utilisé pour créer une fonction mise en cache appelée `dispatchError`, qui met à jour la variable d'état `error` et retourne la nouvelle fonction. Ce hook prend une fonction et un tableau de dépendances en arguments. Dans ce cas, la fonction prend un argument `err`, qui est le nouvel objet d'erreur à envoyer. Le tableau de dépendances est `[]`, ce qui signifie que la fonction mise en cache ne sera recréée que si le composant est re-rendu.

Voici un exemple d'utilisation du hook `useError()` dans un composant :

1. Créez un nouveau composant appelé `ErrorButton`.

2. À l'intérieur du composant, appelez le hook `useError()` pour obtenir la fonction `dispatchError`.

3. Créez une fonction de gestionnaire de clic appelée `clickHandler` qui appelle `dispatchError` avec un nouvel objet d'erreur.

4. Rendez un bouton qui appelle `clickHandler` lorsqu'il est cliqué.

Voici le code :

```jsx
const useError = (err = null) => {
  const [error, setError] = React.useState(err);

  React.useEffect(() => {
    if (error) {
      throw error;
    }
  }, [error]);

  const dispatchError = React.useCallback((err) => {
    setError(err);
  }, []);

  return dispatchError;
};

const ErrorButton = () => {
  const dispatchError = useError();

  const clickHandler = () => {
    dispatchError(new Error("Error!"));
  };

  return <button onClick={clickHandler}>Throw error</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ErrorButton />);
```

Veuillez cliquer sur « Go Live » dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
