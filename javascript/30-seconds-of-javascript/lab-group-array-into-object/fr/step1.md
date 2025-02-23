# Comment regrouper un tableau en un objet

Pour regrouper un tableau en un objet, suivez ces étapes :

1. Ouvrez le Terminal ou SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Array.prototype.reduce()` pour construire un objet à partir des deux tableaux.
3. Fournissez un tableau d'identifiants de propriété valides et un tableau de valeurs.
4. Si la longueur du tableau de propriétés est plus longue que le tableau de valeurs, les clés restantes seront définies sur `undefined`.
5. Si la longueur du tableau de valeurs est plus longue que le tableau de propriétés, les valeurs restantes seront ignorées.

Voici un extrait de code d'exemple qui montre comment regrouper un tableau en un objet :

```js
const zipObject = (props, values) =>
  props.reduce((obj, prop, index) => ((obj[prop] = values[index]), obj), {});

zipObject(["a", "b", "c"], [1, 2]); // {a: 1, b: 2, c: undefined}
zipObject(["a", "b"], [1, 2, 3]); // {a: 1, b: 2}
```
