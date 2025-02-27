# Utilisation des hooks

> Le projet React a déjà été fourni dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code dans `App.js`.

Utilisez la commande suivante pour installer les dépendances :

```bash
npm i
```

Les fonctions commençant par `use` sont appelées Hooks. `useState` est un Hook intégré fourni par React. Vous pouvez trouver d'autres Hooks intégrés dans la référence de l'API. Vous pouvez également écrire vos propres Hooks en combinant les existants.

Les Hooks sont plus restrictifs que les autres fonctions. Vous ne pouvez appeler les Hooks qu'au sommet de vos composants (ou d'autres Hooks). Si vous voulez utiliser `useState` dans une condition ou une boucle, extrayez un nouveau composant et mettez-le là.

Dans l'exemple précédent, chaque `MyButton` avait sa propre `count` indépendante, et lorsqu'un bouton était cliqué, seule la `count` du bouton cliqué changeait :

![Ne pas utiliser les hooks](../assets/1.png)

Cependant, souvent, vous aurez besoin que les composants partagent des données et se mettent à jour ensemble.

Pour que les deux composants `MyButton` affichent le même compte et se mettent à jour ensemble, vous devez déplacer l'état des boutons individuels "vers le haut" jusqu'au composant le plus proche les contenant tous.

Dans cet exemple, c'est `MyApp` :

![Utiliser les hooks](../assets/2.png)

Maintenant, lorsque vous cliquez sur l'un des boutons, la `count` dans `MyApp` changera, ce qui changera les deux `count` dans `MyButton`. Voici comment vous pouvez l'exprimer dans le code.

Tout d'abord, déplacez l'état vers le haut de `MyButton` dans `MyApp` :

```js
// App.js
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Compteurs qui se mettent à jour séparément</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  //... nous déplaçons le code d'ici...
}
```

Ensuite, passez l'état de `MyApp` à chaque `MyButton`, ainsi que le gestionnaire de clic partagé. Vous pouvez passer des informations à `MyButton` en utilisant les accolades JSX, tout comme vous l'avez fait précédemment avec des balises intégrées comme `<img>` :

```js
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Compteurs qui se mettent à jour ensemble</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}
```

L'information que vous passez ainsi est appelée `props`. Maintenant, le composant `MyApp` contient l'état `count` et le gestionnaire d'événement `handleClick`, et les passe tous les deux en tant que `props` à chacun des boutons.

Enfin, modifiez `MyButton` pour lire les `props` que vous avez passées de son composant parent :

```js
function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicé {count} fois</button>;
}
```

Lorsque vous cliquez sur le bouton, le gestionnaire `onClick` est déclenché. La `onClick` prop de chaque bouton a été définie sur la fonction `handleClick` à l'intérieur de `MyApp`, donc le code à l'intérieur de celle-ci s'exécute. Ce code appelle `setCount(count + 1)`, incrémentant la variable d'état `count`. La nouvelle valeur de `count` est passée en tant que `prop` à chaque bouton, donc ils affichent tous la nouvelle valeur. Cela s'appelle "lever l'état vers le haut". En déplaçant l'état vers le haut, vous l'avez partagé entre les composants.

```js
import { useState } from "react";

export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Compteurs qui se mettent à jour ensemble</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}

function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicé {count} fois</button>;
}
```

Pour exécuter le projet, utilisez la commande suivante. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.

```bash
npm start
```
