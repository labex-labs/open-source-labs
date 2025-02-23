# Comment hacher une chaîne de caractères en un nombre à l'aide de JavaScript

Pour hacher une chaîne d'entrée en un nombre entier à l'aide de JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez les méthodes `String.prototype.split()` et `Array.prototype.reduce()` pour créer un hachage de la chaîne d'entrée, en utilisant le décalage binaire.
3. Voici le code pour la fonction `sdbm` qui implémente l'algorithme de hachage :

```js
const sdbm = (str) => {
  let arr = str.split("");
  return arr.reduce(
    (hashCode, currentVal) =>
      (hashCode =
        currentVal.charCodeAt(0) +
        (hashCode << 6) +
        (hashCode << 16) -
        hashCode),
    0
  );
};
```

4. Pour tester la fonction, appelez-la avec un argument de chaîne de caractères :

```js
sdbm("name"); // -3521204949
```

Cela retournera la valeur de hachage pour la chaîne d'entrée "name".
