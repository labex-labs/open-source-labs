# Rendu de listes

> Le projet React a déjà été fourni dans la machine virtuelle (VM). En général, vous n'avez qu'à ajouter du code dans `App.js`.

Veuillez utiliser la commande suivante pour installer les dépendances :

```bash
npm i
```

Vous allez vous appuyer sur des fonctionnalités JavaScript telles que la boucle `for` et la fonction `map()` des tableaux pour afficher des listes de composants.

Par exemple, disons que vous avez un tableau de produits :

```js
const products = [
  { title: "Cabbage", id: 1 },
  { title: "Garlic", id: 2 },
  { title: "Apple", id: 3 }
];
```

À l'intérieur de votre composant, utilisez la fonction `map()` pour transformer un tableau de produits en un tableau d'éléments `<li>` :

```js
const listItems = products.map((product) => (
  <li key={product.id}>{product.title}</li>
));

return <ul>{listItems}</ul>;
```

Remarquez comment `<li>` a un attribut `key`. Pour chaque élément d'une liste, vous devez passer une chaîne de caractères ou un nombre qui identifie de manière unique cet élément parmi ses frères et sœurs. Habituellement, une clé (`key`) devrait provenir de vos données, comme un identifiant de base de données. React utilise vos clés pour savoir ce qui s'est passé si vous insérez, supprimez ou réordonnez les éléments plus tard.

```js
// App.js
const products = [
  { title: "Cabbage", isFruit: false, id: 1 },
  { title: "Garlic", isFruit: false, id: 2 },
  { title: "Apple", isFruit: true, id: 3 }
];

export default function ShoppingList() {
  const listItems = products.map((product) => (
    <li
      key={product.id}
      style={{
        color: product.isFruit ? "magenta" : "darkgreen"
      }}
    >
      {product.title}
    </li>
  ));

  return <ul>{listItems}</ul>;
}
```

Pour exécuter le projet, utilisez la commande suivante. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.

```bash
npm start
```
