# Création et imbrication de composants

> Le projet React a déjà été fourni dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code dans `App.js`.

Utilisez la commande suivante pour installer les dépendances :

```bash
npm i
```

Les applications React sont composées de composants. Un composant est une partie de l'interface utilisateur (UI) qui a sa propre logique et apparence. Un composant peut être aussi petit qu'un bouton, ou aussi grand qu'une page entière.

Les composants React sont des fonctions JavaScript qui renvoient une balise :

```js
// App.js
function MyButton() {
  return <button>I'm a button</button>;
}
```

Maintenant que vous avez déclaré `MyButton`, vous pouvez l'imbriquer dans un autre composant :

```js
// App.js
export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}
```

Remarquez que `<MyButton />` commence par une lettre majuscule. C'est ainsi que vous savez qu'il s'agit d'un composant React. Les noms de composants React doivent toujours commencer par une lettre majuscule, tandis que les balises HTML doivent être en minuscules.

Le mot clé `export default` spécifie le composant principal dans le fichier. Si vous n'êtes pas familier avec une partie de la syntaxe JavaScript, [MDN](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export) et [javascript.info](https://javascript.info/import-export) ont de très bonnes références.

Pour exécuter le projet, utilisez la commande suivante. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.

```bash
npm start
```
