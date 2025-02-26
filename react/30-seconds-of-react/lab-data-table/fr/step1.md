# Tableau de données

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Créez un élément de tableau avec deux colonnes, `ID` et `Valeur`, où chaque ligne est générée dynamiquement à partir d'un tableau de valeurs primitives.

Pour y parvenir, utilisez la méthode `Array.prototype.map()` pour créer un nouveau tableau d'éléments JSX représentant chaque élément du tableau d'entrée `data` en tant qu'élément `<tr>` avec une `key` appropriée. Dans chaque `<tr>`, ajoutez deux éléments `<td>` pour afficher respectivement l'index et la valeur de la ligne.

Voici une implémentation d'exemple :

```jsx
const DataTable = ({ data }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Valeur</th>
        </tr>
      </thead>
      <tbody>
        {data.map((val, i) => (
          <tr key={`${i}_${val}`}>
            <td>{i}</td>
            <td>{val}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

Pour utiliser ce composant avec un tableau de noms de personnes, par exemple, vous pouvez l'appeler comme suit :

```jsx
const people = ["John", "Jesse"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <DataTable data={people} />
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
