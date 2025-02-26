# React useDelayedState Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour retarder la création d'une valeur avec état jusqu'à ce qu'une condition soit remplie, suivez ces étapes :

1. Utilisez le hook `useState()` pour créer une valeur avec état contenant l'`état` réel et un booléen, `chargé`.
2. Utilisez le hook `useEffect()` pour mettre à jour la valeur avec état si la `condition` ou `chargé` change.
3. Créez une fonction, `mise à jour de l'état`, qui ne met à jour la valeur de l'`état` que si `chargé` est vrai.

```jsx
const useDelayedState = (étatInitial, condition) => {
  const [{ état, chargé }, setState] = React.useState({
    état: null,
    chargé: false
  });

  React.useEffect(() => {
    if (!chargé && condition) setState({ état: étatInitial, chargé: true });
  }, [condition, chargé]);

  const mise à jour de l'état = (nouvel État) => {
    if (!chargé) return;
    setState({ état: nouvel État, chargé });
  };

  return [état, mise à jour de l'état];
};
```

Voici un exemple d'utilisation du hook `useDelayedState` :

```jsx
const App = () => {
  const [branches, setBranches] = React.useState([]);
  const [selectedBranch, setSelectedBranch] = useDelayedState(
    branches[0],
    branches.length
  );

  React.useEffect(() => {
    const handle = setTimeout(() => {
      setBranches(["master", "staging", "test", "dev"]);
    }, 2000);
    return () => {
      handle && clearTimeout(handle);
    };
  }, []);

  return (
    <div>
      <p>Selected branch: {selectedBranch}</p>
      <select onChange={(e) => setSelectedBranch(e.target.value)}>
        {branches.map((branch) => (
          <option key={branch} value={branch}>
            {branch}
          </option>
        ))}
      </select>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
