# React useInterval Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour implémenter `setInterval()` de manière déclarative, vous pouvez créer un hook personnalisé qui prend une `callback` et un `delay`. La première étape consiste à utiliser le hook `useRef()` pour créer une `ref` pour la fonction de rappel. Ensuite, utilisez un hook `useEffect()` pour vous souvenir de la dernière `callback` chaque fois qu'elle change. Enfin, utilisez un hook `useEffect()` dépendant de `delay` pour configurer l'intervalle et le nettoyer.

Voici un extrait de code d'exemple pour le hook personnalisé :

```jsx
const useInterval = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    };
    if (delay !== null) {
      let id = setInterval(tick, delay);
      return () => clearInterval(id);
    }
  }, [delay]);
};
```

Vous pouvez ensuite utiliser ce hook personnalisé dans vos composants. Par exemple, pour créer un temporisateur qui se met à jour toutes les secondes :

```jsx
const Timer = (props) => {
  const [seconds, setSeconds] = React.useState(0);

  useInterval(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Timer />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
