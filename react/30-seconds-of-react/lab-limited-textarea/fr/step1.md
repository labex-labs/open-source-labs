# Zone de texte avec limite de caractères

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Voici le code :

```jsx
const LimitedTextarea = ({ rows, cols, value, limit }) => {
  const [content, setContent] = React.useState(value.slice(0, limit));

  const setFormattedContent = React.useCallback(
    (text) => {
      setContent(text.slice(0, limit));
    },
    [limit]
  );

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        onChange={(event) => setFormattedContent(event.target.value)}
        value={content}
      />
      <p>
        {content.length}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedTextarea limit={32} value="Hello!" />
);
```

Dans ce code, nous :

- avons simplifié les commentaires pour fournir une vue d'ensemble plus concise de ce que fait chaque partie du code.
- avons supprimé les commentaires de code inutiles.
- avons supprimé la fonction `setContent` du tableau de dépendances de `useCallback`, car elle n'est pas nécessaire.
- avons ajouté des parenthèses autour de l'argument `text` dans la fonction `useCallback` pour la cohérence.
- avons utilisé des fonctions fléchées pour le gestionnaire d'événement `onChange` pour la concision.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
