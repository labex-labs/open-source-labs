# Hook useMutationObserver de React

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle (VM). En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour surveiller les modifications apportées à l'arbre DOM, le hook `useMutationObserver` peut être utilisé. Voici comment il fonctionne :

1. Le hook prend trois paramètres : `ref`, `callback` et `options`.
2. À l'intérieur du hook, un hook `useEffect()` est utilisé, qui dépend des valeurs de `callback` et `options`.
3. Si la `ref` donnée est initialisée, un nouveau `MutationObserver` est créé et la fonction de rappel (`callback`) lui est passée.
4. `MutationObserver.observe()` est appelé avec les `options` données pour surveiller la `ref` donnée pour détecter les modifications.
5. `MutationObserver.disconnect()` est utilisé pour supprimer l'observateur de la `ref` lorsque le composant est démonté.

Voici le code :

```jsx
const useMutationObserver = (
  ref,
  callback,
  options = {
    attributes: true,
    characterData: true,
    childList: true,
    subtree: true
  }
) => {
  React.useEffect(() => {
    if (!ref.current) return;

    const observer = new MutationObserver(callback);
    observer.observe(ref.current, options);

    return () => observer.disconnect();
  }, [callback, options, ref]);
};
```

Dans le composant `App`, le hook `useMutationObserver` est utilisé pour surveiller les modifications apportées à l'élément `mutationRef`. La fonction `incrementMutationCount` est passée en tant que fonction de rappel (`callback`).

```jsx
const App = () => {
  const mutationRef = React.useRef();
  const [mutationCount, setMutationCount] = React.useState(0);

  const incrementMutationCount = React.useCallback(() => {
    setMutationCount((count) => count + 1);
  }, []);

  useMutationObserver(mutationRef, incrementMutationCount);

  const [content, setContent] = React.useState("Hello world");

  return (
    <>
      <label htmlFor="content-input">Edit this to update the text:</label>
      <textarea
        id="content-input"
        style={{ width: "100%" }}
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
      <div style={{ width: "100%" }} ref={mutationRef}>
        <div
          style={{
            resize: "both",
            overflow: "auto",
            maxWidth: "100%",
            border: "1px solid black"
          }}
        >
          <h2>Resize or change the content:</h2>
          <p>{content}</p>
        </div>
      </div>
      <div>
        <h3>Mutation count {mutationCount}</h3>
      </div>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
