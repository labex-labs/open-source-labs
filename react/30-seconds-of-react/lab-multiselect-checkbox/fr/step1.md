# Case à cocher avec état et sélection multiple

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce code affiche une liste de cases à cocher et envoie la valeur ou les valeurs sélectionnées au composant parent à l'aide d'une fonction de rappel. Voici les étapes pour la créer :

1. Utilisez le hook `useState()` pour initialiser la variable d'état `data` avec la propriété `options`.
2. Créez une fonction `toggle` qui met à jour la variable d'état `data` avec l'option ou les options sélectionnées et appelle la fonction de rappel `onChange` avec elles.
3. Map la variable d'état `data` pour générer des cases à cocher individuelles et leurs étiquettes. Associez la fonction `toggle` au gestionnaire `onClick` de chaque case à cocher.

```jsx
const MultiselectCheckbox = ({ options, onChange }) => {
  const [data, setData] = React.useState(options);

  const toggle = (index) => {
    const newData = [...data];
    newData[index] = {
      ...newData[index],
      checked: !newData[index].checked
    };
    setData(newData);
    onChange(newData.filter((item) => item.checked));
  };

  return (
    <>
      {data.map((item, index) => (
        <label key={item.label}>
          <input
            type="checkbox"
            checked={item.checked || false}
            onChange={() => toggle(index)}
          />
          {item.label}
        </label>
      ))}
    </>
  );
};
```

Voici un exemple d'utilisation :

```jsx
const options = [{ label: "Item One" }, { label: "Item Two" }];

ReactDOM.createRoot(document.getElementById("root")).render(
  <MultiselectCheckbox
    options={options}
    onChange={(selected) => {
      console.log(selected);
    }}
  />
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
