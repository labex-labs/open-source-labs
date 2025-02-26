# React useComponentDidUpdate Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce code fournit un hook personnalisé appelé `useComponentDidUpdate` qui exécute une fonction `callback` fournie chaque fois qu'un composant est mis à jour. Voici les étapes suivies par le hook :

1. Créez une variable `mounted` à l'aide du hook `useRef()`. Cette variable suit si le composant a été monté ou non.
2. Utilisez le hook `useEffect()` pour définir la valeur de `mounted` sur `true` lors de la première exécution du hook.
3. Dans les exécutions suivantes du hook, exécutez la fonction `callback` fournie seulement si le composant a déjà été monté.
4. Si un deuxième argument `condition` est fourni, le hook ne s'exécutera que si l'un de ses dépendances change.
5. Ce hook se comporte comme la méthode de cycle de vie `componentDidUpdate()` des composants de classe.

Voici le code :

```jsx
const useComponentDidUpdate = (callback, condition) => {
  const isMounted = React.useRef(false);
  React.useEffect(() => {
    if (isMounted.current) {
      callback();
    } else {
      isMounted.current = true;
    }
  }, condition);
};

const App = () => {
  const [value, setValue] = React.useState(0);
  const [otherValue, setOtherValue] = React.useState(1);

  useComponentDidUpdate(() => {
    console.log(`La valeur actuelle est ${value}.`);
  }, [value]);

  return (
    <>
      <p>
        Valeur : {value}, autre valeur : {otherValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Incrémenter la valeur</button>
      <button onClick={() => setOtherValue(otherValue + 1)}>
        Incrémenter l'autre valeur
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
