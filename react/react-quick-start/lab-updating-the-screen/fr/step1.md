# Mise à jour de l'écran

> Le projet React a déjà été fourni dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code dans `App.js`.

Utilisez la commande suivante pour installer les dépendances :

```bash
npm i
```

Souvent, vous voudrez que votre composant "se souvienne" de certaines informations et les affiche. Par exemple, peut-être que vous voulez compter le nombre de fois qu'un bouton est cliqué. Pour ce faire, ajoutez un état à votre composant.

Tout d'abord, importez `useState` de React :

```js
import { useState } from "react";
```

Maintenant, vous pouvez déclarer une variable d'état à l'intérieur de votre composant :

```js
function MyButton() {
  const [count, setCount] = useState(0);
  //...
```

Vous obtiendrez deux choses de `useState` : l'état actuel (`count`), et la fonction qui vous permet de le mettre à jour (`setCount`). Vous pouvez leur donner n'importe quel nom, mais la convention est d'écrire `[quelqueChose, setQuelqueChose]`.

La première fois que le bouton est affiché, `count` sera `0` car vous avez passé 0 à `useState()`. Lorsque vous voulez changer l'état, appelez `setCount()` et passez la nouvelle valeur à celle-ci. Cliquez sur ce bouton pour incrémenter le compteur :

```js
function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

React appellera à nouveau votre fonction de composant. Cette fois, `count` sera `1`. Puis ce sera `2`. Et ainsi de suite.

Si vous rendez le même composant plusieurs fois, chacun aura son propre état. Cliquez séparément sur chaque bouton :

```js
// App.js
import { useState } from "react";

export default function MyApp() {
  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

Remarquez comment chaque bouton "se souvient" de son propre état `count` et n'affecte pas les autres boutons.

Pour exécuter le projet, utilisez la commande suivante. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.

```bash
npm start
```
