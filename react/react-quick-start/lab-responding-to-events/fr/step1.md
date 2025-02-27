# Répondre aux événements

> Le projet React a déjà été fourni dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `App.js`.

Utilisez la commande suivante pour installer les dépendances :

```bash
npm i
```

React vous permet d'ajouter des gestionnaires d'événements à votre JSX. Les gestionnaires d'événements sont vos propres fonctions qui seront déclenchées en réponse à des interactions telles que le clic, le survol, la mise au point des entrées du formulaire, etc.

Pour ajouter un gestionnaire d'événements, vous devrez d'abord définir une fonction puis [la passer en tant que propriété](https://react.dev/learn/passing-props-to-a-component) à la balise JSX appropriée. Par exemple, voici un bouton qui ne fait rien pour le moment :

```js
// App.js
export default function Button() {
  return <button>Je ne fais rien</button>;
}
```

Vous pouvez le faire afficher un message lorsqu'un utilisateur clique en suivant ces trois étapes :

1. Décarez une fonction appelée `handleClick` à l'intérieur de votre composant `Button`.
2. Implémentez la logique à l'intérieur de cette fonction (utilisez `alert` pour afficher le message).
3. Ajoutez `onClick={handleClick}` à la balise JSX `<button>`.

```js
export default function Button() {
  function handleClick() {
    alert("Vous m'avez cliqué!");
  }

  return <button onClick={handleClick}>Cliquez sur moi</button>;
}
```

Vous avez défini la fonction `handleClick` puis l'avez passée en tant que propriété à `<button>`. `handleClick` est un gestionnaire d'événements. Les fonctions de gestionnaire d'événements :

Sont généralement définies à l'intérieur de vos composants.
Ont des noms qui commencent par `handle`, suivi du nom de l'événement.

Pour exécuter le projet, utilisez la commande suivante. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.

```bash
npm start
```

Par convention, il est courant de nommer les gestionnaires d'événements `handle` suivi du nom de l'événement. Vous verrez souvent `onClick={handleClick}`, `onMouseEnter={handleMouseEnter}`, etc.

Alternativement, vous pouvez définir un gestionnaire d'événements en ligne dans le JSX :

```js
<button onClick={function handleClick() {
  alert('Vous m'avez cliqué!');
}}>
```

Ou, plus concisément, en utilisant une fonction fléchée :

```js
<button onClick={() => {
  alert('Vous m'avez cliqué!');
}}>
```

Tous ces styles sont équivalents. Les gestionnaires d'événements en ligne sont pratiques pour les fonctions courtes.
