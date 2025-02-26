# Élément `<select>` non contrôlé

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Il s'agit d'un composant qui affiche un élément `<select>` contrôlé. Le composant accepte un tableau de valeurs et une fonction de rappel pour passer la valeur sélectionnée à son composant parent. Voici les étapes pour utiliser ce composant :

- Utilisez la propriété `selectedValue` pour définir la valeur initiale de l'élément `<select>`.
- Utilisez la propriété `onValueChange` pour spécifier la fonction de rappel qui doit être appelée lorsque la valeur de l'élément `<select>` change.
- Utilisez `Array.prototype.map()` sur le tableau `values` pour créer un élément `<option>` pour chaque valeur passée.
- Chaque élément de `values` doit être un tableau à deux éléments, où le premier élément est la `valeur` de l'élément et le second est le texte affiché pour celui-ci.

```jsx
const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
  return (
    <select
      defaultValue={selectedValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    >
      {values.map(([value, text]) => (
        <option key={value} value={value}>
          {text}
        </option>
      ))}
    </select>
  );
};
```

Voici un exemple d'utilisation de ce composant :

```jsx
const choices = [
  ["grapefruit", "Pamplemousse"],
  ["lime", "Citron vert"],
  ["coconut", "Coco"],
  ["mango", "Mangue"]
];

ReactDOM.createRoot(document.getElementById("root")).render(
  <Select
    values={choices}
    selectedValue="lime"
    onValueChange={(val) => console.log(val)}
  />
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
