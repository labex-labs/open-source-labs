# Basculer l'affichage/cachage du mot de passe

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Le code suivant affiche un champ de saisie de mot de passe avec un bouton d'affichage. Il utilise le hook `useState()` pour créer la variable d'état `shown` et définir sa valeur initiale sur `false`. Lorsque le bouton `Afficher/Cacher` est cliqué, la fonction `setShown` est appelée, basculant le `type` de l'input entre `'text'` et `'password'`.

```jsx
const PasswordRevealer = ({ value }) => {
  const [shown, setShown] = React.useState(false);
  return (
    <>
      <input type={shown ? "text" : "password"} value={value} />
      <button onClick={() => setShown(!shown)}>Afficher/Cacher</button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <PasswordRevealer />
);
```

Veuillez cliquer sur 'Démarrer' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
