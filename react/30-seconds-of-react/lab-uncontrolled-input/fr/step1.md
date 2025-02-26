# Champ d'entrée non contrôlé

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce code affiche un élément `<input>` non contrôlé qui utilise une fonction de rappel pour informer son parent des mises à jour de valeur. Pour l'utiliser :

- Passez la valeur initiale depuis le parent en utilisant la propriété `defaultValue`.
- Passez une fonction de rappel appelée `onValueChange` pour gérer les mises à jour de valeur.
- Utilisez l'événement `onChange` pour déclencher la fonction de rappel et envoyer la nouvelle valeur au parent.

Voici un exemple :

```jsx
const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
  return (
    <input
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <UncontrolledInput
    type="text"
    placeholder="Insérez du texte ici..."
    onValueChange={console.log}
  />
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
