# React useHash Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce code suit et met à jour la valeur du hash de l'emplacement du navigateur. Pour l'utiliser, suivez ces étapes :

1. Utilisez le hook `useState()` pour obtenir de manière paresseuse la propriété `hash` de l'objet `Location`.
2. Utilisez le hook `useCallback()` pour créer un gestionnaire qui met à jour l'état `hash` lorsque l'événement `'hashchange'` est déclenché.
3. Utilisez le hook `useEffect()` pour ajouter un écouteur pour l'événement `'hashchange'` lors du montage et le nettoyer lors du démontage.
4. Utilisez le hook `useCallback()` pour créer une fonction qui met à jour la propriété `hash` de l'objet `Location` avec la valeur donnée.
5. Dans votre composant, appelez `useHash()` pour obtenir la valeur `hash` actuelle et une fonction `updateHash()` pour la modifier.
6. Utilisez la fonction `updateHash()` pour changer la valeur du hash.
7. Affichez la valeur `hash` actuelle dans un composant.
8. Créez un champ de saisie permettant à l'utilisateur de changer la valeur du hash.

Voici le code :

```jsx
const useHash = () => {
  const [hash, setHash] = React.useState(() => window.location.hash);

  const hashChangeHandler = React.useCallback(() => {
    setHash(window.location.hash);
  }, []);

  React.useEffect(() => {
    window.addEventListener("hashchange", hashChangeHandler);
    return () => {
      window.removeEventListener("hashchange", hashChangeHandler);
    };
  }, []);

  const updateHash = React.useCallback(
    (newHash) => {
      if (newHash !== hash) window.location.hash = newHash;
    },
    [hash]
  );

  return [hash, updateHash];
};

const MyApp = () => {
  const [hash, setHash] = useHash();

  React.useEffect(() => {
    setHash("#list");
  }, []);

  return (
    <>
      <p>Valeur du hash actuelle : {hash}</p>
      <p>Modifier le hash : </p>
      <input value={hash} onChange={(e) => setHash(e.target.value)} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
