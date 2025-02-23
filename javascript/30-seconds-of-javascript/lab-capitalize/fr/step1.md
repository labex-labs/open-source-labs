# JavaScript Function to Capitalize First Letter of a String

Pour mettre en majuscule la première lettre d'une chaîne de caractères en JavaScript, utilisez la fonction suivante :

```js
const capitalize = (str, lowerRest = false) => {
  const [first, ...rest] = str;
  return (
    first.toUpperCase() +
    (lowerRest ? rest.join("").toLowerCase() : rest.join(""))
  );
};
```

Cette fonction utilise la décomposition d'un tableau et `String.prototype.toUpperCase()` pour mettre en majuscule la première lettre de la chaîne. L'argument `lowerRest` est facultatif et peut être défini sur `true` pour convertir le reste de la chaîne en minuscules.

Voici un exemple d'utilisation de cette fonction :

```js
capitalize("fooBar"); // 'FooBar'
capitalize("fooBar", true); // 'Foobar'
```
