# React useEffectOnce Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Le code ci-dessous implémente une fonction `useEffectOnce(callback, when)` qui exécute une `callback` seulement une fois lorsqu'une condition `when` devient vraie.

Pour implémenter cette fonction :

- Créez une variable `hasRunOnce` en utilisant le hook `useRef()` pour suivre l'état d'exécution de l'effet.
- Utilisez le hook `useEffect()` qui s'exécute seulement lorsque la condition `when` change.
- À l'intérieur du hook `useEffect()`, vérifiez si `when` est `true` et que l'effet n'a pas été exécuté auparavant. Si les deux conditions sont vraies, exécutez `callback` et définissez `hasRunOnce` sur `true`.

```jsx
const useEffectOnce = (callback, when) => {
  const hasRunOnce = React.useRef(false);
  React.useEffect(() => {
    if (when && !hasRunOnce.current) {
      callback();
      hasRunOnce.current = true;
    }
  }, [when]);
};
```

Voici un exemple d'utilisation de `useEffectOnce()` :

```jsx
const App = () => {
  const [clicked, setClicked] = React.useState(false);
  useEffectOnce(() => {
    console.log("monté");
  }, clicked);
  return <button onClick={() => setClicked(true)}>Cliquez sur moi</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Dans l'exemple, `useEffectOnce()` est utilisé pour afficher "monté" dans la console lorsque le bouton est cliqué pour la première fois. Le hook `useEffectOnce()` est passé deux arguments : la `callback` à exécuter et la condition `when` à vérifier. La condition `when` est définie sur l'état `clicked`, donc la `callback` s'exécute seulement lorsque `clicked` est `true` pour la première fois.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
