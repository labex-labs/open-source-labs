# Comment obtenir le dernier élément d'un tableau en JavaScript

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`. La fonction suivante renvoie le dernier élément d'un tableau :

```js
const last = (arr) => (arr && arr.length ? arr[arr.length - 1] : undefined);
```

Pour l'utiliser, vous devez fournir un tableau en tant qu'argument. La fonction vérifie si le tableau est évalué comme vrai et a une propriété `length`. Si les deux conditions sont vraies, elle calcule l'index du dernier élément du tableau et le renvoie. Sinon, elle renvoie `undefined`.

Voici quelques exemples :

```js
last([1, 2, 3]); // 3
last([]); // undefined
last(null); // undefined
last(undefined); // undefined
```
