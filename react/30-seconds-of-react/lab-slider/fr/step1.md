# Entrée de plage non contrôlée

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour créer un curseur dans React, utilisez le composant `Slider` et passez les props `min`, `max`, `defaultValue` et `onValueChange`.

Dans le composant `Slider`, définissez le `type` de l'élément `<input>` sur `"range"` pour créer un curseur. Utilisez la prop `defaultValue` transmise par le parent comme valeur initiale du champ d'entrée non contrôlé. Utilisez l'événement `onChange` pour déclencher la fonction de rappel `onValueChange` et envoyer la nouvelle valeur au parent.

Voici le code pour le composant `Slider`:

```jsx
const Slider = ({
  min = 0,
  max = 100,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <input
      type="range"
      min={min}
      max={max}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

Pour rendre le composant `Slider`, utilisez `ReactDOM.createRoot` et passez la fonction de rappel `onValueChange`:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Slider onValueChange={(val) => console.log(val)} />
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
