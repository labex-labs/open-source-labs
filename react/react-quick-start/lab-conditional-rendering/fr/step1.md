# Affichage conditionnel

> Le projet React a déjà été fourni dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code dans `App.js`.

Utilisez la commande suivante pour installer les dépendances :

```bash
npm i
```

En React, il n'y a pas de syntaxe spéciale pour écrire des conditions. Au lieu de cela, vous utiliserez les mêmes techniques que celles que vous utilisez lorsqu vous écrivez du code JavaScript classique. Par exemple, vous pouvez utiliser une instruction `if` pour inclure conditionnellement du JSX :

```js
if (isPacked) {
  return <li className="item">{name} ✔</li>;
}
return <li className="item">{name}</li>;
```

Si vous préférez un code plus compact, vous pouvez utiliser l'opérateur conditionnel `?`. Contrairement à `if`, il fonctionne à l'intérieur du JSX :

```js
return <li className="item">{isPacked ? name + " ✔" : name}</li>;
```

Lorsque vous n'avez pas besoin de la branche `else`, vous pouvez également utiliser une syntaxe logique `&&` plus courte :

```js
return <li className="item">{isPacked && name + " ✔"}</li>;
```

Si la propriété `isPacked` est vraie, ce code renvoie un arbre JSX différent. Avec ce changement, certains des éléments ont une croix de vérification à la fin :

```js
// App.js
function Item({ name, isPacked }) {
  if (isPacked) {
    return <li className="item">{name} ✔</li>;
  }
  return <li className="item">{name}</li>;
}

export default function PackingList() {
  return (
    <section>
      <h1>Liste d'équipement de Sally Ride</h1>
      <ul>
        <Item isPacked={true} name="Costume spatial" />
        <Item isPacked={true} name="Casque avec une feuille d'or" />
        <Item isPacked={false} name="Photo de Tam" />
      </ul>
    </section>
  );
}
```

Pour exécuter le projet, utilisez la commande suivante. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.

```bash
npm start
```
