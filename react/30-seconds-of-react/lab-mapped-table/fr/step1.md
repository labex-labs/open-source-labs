# Vue d'affichage de table d'objets

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Ce composant affiche un tableau dont les lignes sont dynamiquement créées à partir d'un tableau d'objets et d'une liste de noms de propriétés. Pour y arriver :

- Utilisez `Object.keys()`, `Array.prototype.filter()`, `Array.prototype.includes()` et `Array.prototype.reduce()` pour produire un tableau `filteredData` qui contient tous les objets avec les clés spécifiées dans `propertyNames`.
- Affichez un élément `<table>` avec un ensemble de colonnes égal au nombre de valeurs dans `propertyNames`.
- Utilisez `Array.prototype.map()` pour afficher chaque valeur dans le tableau `propertyNames` en tant qu'élément `<th>`.
- Utilisez `Array.prototype.map()` pour afficher chaque objet dans le tableau `filteredData` en tant qu'élément `<tr>` contenant un `<td>` pour chaque clé de l'objet.
- Notez que ce composant ne fonctionne pas avec les objets imbriqués et se casserait s'il y a des objets imbriqués dans l'une des propriétés spécifiées dans `propertyNames`.

Voici le code :

```jsx
const MappedTable = ({ data, propertyNames }) => {
  const filteredData = data.map((obj) =>
    Object.keys(obj)
      .filter((key) => propertyNames.includes(key))
      .reduce((acc, key) => ({ ...acc, [key]: obj[key] }), {})
  );

  return (
    <table>
      <thead>
        <tr>
          {propertyNames.map((name) => (
            <th key={`header-${name}`}>{name}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {filteredData.map((obj, i) => (
          <tr key={`row-${i}`}>
            {propertyNames.map((name) => (
              <td key={`cell-${i}-${name}`}>{obj[name]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

Vous pouvez utiliser le composant en passant un tableau d'objets et une liste de noms de propriétés :

```jsx
const people = [
  { name: "John", surname: "Smith", age: 42 },
  { name: "Adam", surname: "Smith", gender: "male" }
];
const propertyNames = ["name", "surname", "age"];

ReactDOM.render(
  <MappedTable data={people} propertyNames={propertyNames} />,
  document.getElementById("root")
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
