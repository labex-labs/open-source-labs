# Champ de saisie contrôlé

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce fragment de code fournit un élément `<input>` contrôlé qui utilise une fonction de rappel pour informer son parent de tout changement de sa valeur. Voici comment cela fonctionne :

- La valeur du champ de saisie contrôlé est déterminée par la propriété `value` transmise par le parent.
- Toute modification effectuée sur le champ de saisie par l'utilisateur est capturée par l'événement `onChange`, qui déclenche la fonction de rappel `onValueChange` et envoie la nouvelle valeur au composant parent.
- Pour mettre à jour la valeur du champ de saisie, le parent doit mettre à jour la propriété `value` qu'il transmet au composant de champ de saisie contrôlé.

Voici une implémentation exemple du composant `ControlledInput`, suivie d'un exemple d'utilisation dans un composant `Form` :

```jsx
const ControlledInput = ({ value, onValueChange, ...rest }) => {
  return (
    <input
      value={value}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

const Form = () => {
  const [value, setValue] = React.useState("");

  return (
    <ControlledInput
      type="text"
      placeholder="Insérez du texte ici..."
      value={value}
      onValueChange={setValue}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Form />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
