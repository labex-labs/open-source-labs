# Élément `<textarea>` non contrôlé

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Cette fonction affiche un élément `<textarea>` qui n'est pas contrôlé par le composant parent. Elle utilise une fonction de rappel pour passer la valeur de l'entrée au composant parent.

Pour utiliser cette fonction :

- Passez la propriété `defaultValue` du composant parent comme valeur initiale du champ de saisie.
- Utilisez l'événement `onChange` pour déclencher la fonction de rappel `onValueChange` et envoyer la nouvelle valeur au parent.

```jsx
const TextArea = ({
  cols = 20,
  rows = 2,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <textarea
      cols={cols}
      rows={rows}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

Utilisation de l'exemple :

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <TextArea
    placeholder="Insérez du texte ici..."
    onValueChange={(val) => console.log(val)}
  />
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
