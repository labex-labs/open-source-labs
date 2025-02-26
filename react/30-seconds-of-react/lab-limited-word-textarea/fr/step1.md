# Zone de texte avec limite de mots

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

```jsx
// Affiche un composant de zone de texte avec une limite de mots.
const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
  const [{ content, wordCount }, setContent] = React.useState({
    content: value,
    wordCount: 0
  });

  // Crée une fonction mémoïsée qui formate le texte d'entrée.
  const setFormattedContent = React.useCallback(
    (text) => {
      const words = text.split(" ").filter(Boolean);
      const truncated = words.slice(0, limit).join(" ");
      setContent({
        content: words.length > limit ? truncated : text,
        wordCount: words.length > limit ? limit : words.length
      });
    },
    [limit, setContent]
  );

  // Appelle setFormattedContent avec la valeur initiale de content.
  React.useEffect(() => {
    setFormattedContent(content);
  }, []);

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        value={content}
        onChange={(event) => setFormattedContent(event.target.value)}
      />
      <p>
        {wordCount}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedWordTextarea limit={5} value="Hello there!" />
);
```

Changements effectués :

- Ajout de commentaires pour expliquer ce que fait chaque partie du code.
- Simplification de la logique dans `setFormattedContent` pour la rendre plus concise.
- Décalage de la fonction `setContent` à la fin de l'appel de fonction pour faciliter la lecture.
- Réordonnement des props dans le composant `<textarea>` pour plus de cohérence.
- Suppression d'espaces et de retours à la ligne inutiles.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
