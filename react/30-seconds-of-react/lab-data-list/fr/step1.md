# Data List

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Cette fonction affiche une liste d'éléments à partir d'un tableau de valeurs primitives. Elle peut être utilisée pour afficher conditionnellement une liste ordonnée ou non ordonnée en fonction de la valeur de la prop `isOrdered`. Pour afficher chaque élément du tableau `data`, elle utilise `Array.prototype.map()` pour créer un élément `<li>` avec une `clé` unique pour chaque élément.

```jsx
const DataList = ({ data, isOrdered = false }) => {
  const list = data.map((value, index) => (
    <li key={`${index}_${value}`}>{value}</li>
  ));

  return isOrdered ? <ol>{list}</ol> : <ul>{list}</ul>;
};
```

Voici un exemple de manière dont vous pouvez utiliser ce composant :

```jsx
const names = ["John", "Paul", "Mary"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <>
    <DataList data={names} />
    <DataList data={names} isOrdered={true} />
  </>
);
```

Dans cet exemple, nous passons un tableau de noms au composant `DataList` et l'affichons deux fois. La première fois, nous affichons une liste non ordonnée, tandis que la seconde fois, nous affichons une liste ordonnée.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
