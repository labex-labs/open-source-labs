# React useCopyToClipboard Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code dans `script.js` et `style.css`.

Pour copier le texte donné dans le presse-papiers, utilisez le bout de code `copyToClipboard` fourni dans `/js/s/copy-to-clipboard/` ainsi que le hook `useState()` pour initialiser la variable `copied`. Pour créer un rappel pour la méthode `copyToClipboard`, utilisez le hook `useCallback()`. Pour réinitialiser la variable d'état `copied` lorsque le `text` change, utilisez le hook `useEffect()`. Enfin, renvoyez la variable d'état `copied` et le rappel `copy`.

Le code suivant démontre un exemple de manière à utiliser ces hooks et méthodes pour créer un composant `TextCopy`. Lorsque l'utilisateur clique sur le bouton "Cliquez pour copier", la fonction `copy` est appelée et la variable `copied` est définie sur `true`. Si la copie est réussie, "Copié!" sera affiché.

```jsx
const useCopyToClipboard = (text) => {
  const copyToClipboard = (str) => {
    const el = document.createElement("textarea");
    el.value = str;
    el.setAttribute("readonly", "");
    el.style.position = "absolute";
    el.style.left = "-9999px";
    document.body.appendChild(el);
    const selected =
      document.getSelection().rangeCount > 0
        ? document.getSelection().getRangeAt(0)
        : false;
    el.select();
    const success = document.execCommand("copy");
    document.body.removeChild(el);
    if (selected) {
      document.getSelection().removeAllRanges();
      document.getSelection().addRange(selected);
    }
    return success;
  };

  const [copied, setCopied] = React.useState(false);

  const copy = React.useCallback(() => {
    if (!copied) setCopied(copyToClipboard(text));
  }, [text]);

  React.useEffect(() => () => setCopied(false), [text]);

  return [copied, copy];
};

const TextCopy = (props) => {
  const [copied, copy] = useCopyToClipboard("Lorem ipsum");

  return (
    <div>
      <button onClick={copy}>Cliquez pour copier</button>
      <span>{copied && "Copié!"}</span>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<TextCopy />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
