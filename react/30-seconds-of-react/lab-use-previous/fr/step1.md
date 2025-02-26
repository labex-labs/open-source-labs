# React usePrevious Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour stocker l'état ou les props précédents, vous pouvez créer un hook personnalisé. Voici les étapes :

1. Définissez un hook personnalisé qui prend un argument `value`.
2. Utilisez le hook `useRef()` pour créer une `ref` pour la `value`.
3. Utilisez le hook `useEffect()` pour retenir la valeur la plus récente de `value`.
4. Retournez la valeur `ref.current`.

```jsx
const usePrevious = (value) => {
  const ref = React.useRef();
  React.useEffect(() => {
    ref.current = value;
  });
  return ref.current;
};
```

Voici un exemple d'utilisation du hook `usePrevious` :

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = usePrevious(value);

  return (
    <div>
      <p>
        Actuel : {value} - Précédent : {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Incrémenter</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Le composant `Counter` affiche les valeurs actuelles et précédentes de `value`. Lorsque le bouton `Incrémenter` est cliqué, `value` est mis à jour et la valeur précédente est stockée à l'aide du hook `usePrevious`.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
