# React useRequestAnimationFrame Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour exécuter une fonction d'animation avant chaque rafraîchissement de l'écran, utilisez le hook `useRef()` pour créer les variables `requestRef` et `previousTimeRef`. Ensuite, définissez une fonction `animate()` qui met à jour ces variables, exécute la `callback` et appelle `Window.requestAnimationFrame()` de manière permanente. Enfin, utilisez le hook `useEffect()` avec un tableau vide pour initialiser la valeur de `requestRef` avec `Window.requestAnimationFrame()`, et utilisez la valeur renvoyée et `Window.cancelAnimationFrame()` pour nettoyer lorsque le composant est démonté.

Voici une implémentation exemple de `useRequestAnimationFrame()` :

```jsx
const useRequestAnimationFrame = (callback) => {
  const requestRef = React.useRef();
  const previousTimeRef = React.useRef();

  const animate = (time) => {
    if (previousTimeRef.current) {
      callback(time - previousTimeRef.current);
    }
    previousTimeRef.current = time;
    requestRef.current = requestAnimationFrame(animate);
  };

  React.useEffect(() => {
    requestRef.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(requestRef.current);
  }, []);
};
```

Pour utiliser ce hook personnalisé dans un composant, passez simplement une fonction de rappel à celui-ci. Par exemple, pour créer un compteur simple qui met à jour à 100 images par seconde :

```jsx
const Counter = () => {
  const [count, setCount] = React.useState(0);

  useRequestAnimationFrame((deltaTime) => {
    setCount((prevCount) => (prevCount + deltaTime * 0.01) % 100);
  });

  return <p>{Math.round(count)}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
