# Comment générer une chaîne alphanumérique aléatoire en JavaScript

Pour générer une chaîne aléatoire de caractères alphanumériques en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Créez un nouveau tableau avec la longueur spécifiée à l'aide de `Array.from()`.
3. Générez un nombre à virgule flottante aléatoire à l'aide de `Math.random()`.
4. Convertissez le nombre en une chaîne alphanumérique à l'aide de `Number.prototype.toString()` avec une valeur de `radix` de `36`.
5. Supprimez la partie entière et la virgule décimale de chaque nombre généré à l'aide de `String.prototype.slice()`.
6. Répétez ce processus autant de fois que nécessaire, jusqu'à `length`, à l'aide de `Array.prototype.some()`, car elle produit une chaîne de longueur variable à chaque fois.
7. Raccourcis la chaîne générée si elle est plus longue que la `length` donnée à l'aide de `String.prototype.slice()`.
8. Retournez la chaîne générée.

Voici le code :

```js
const randomAlphaNumeric = (length) => {
  let s = "";
  Array.from({ length }).some(() => {
    s += Math.random().toString(36).slice(2);
    return s.length >= length;
  });
  return s.slice(0, length);
};
```

Vous pouvez appeler la fonction `randomAlphaNumeric()` avec la longueur souhaitée en tant qu'argument. Par exemple :

```js
randomAlphaNumeric(5); // '0afad'
```
