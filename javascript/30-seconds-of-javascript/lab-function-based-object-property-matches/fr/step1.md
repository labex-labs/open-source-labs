# Correspondance de propriétés d'objet avec une fonction

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Cette fonction compare deux objets et vérifie si le premier objet contient des valeurs de propriété équivalentes à celles du second. Elle le fait sur la base d'une fonction fournie.

Pour utiliser cette fonction, suivez ces étapes :

- Utilisez `Object.keys()` pour récupérer toutes les clés du second objet.
- Utilisez `Array.prototype.every()`, `Object.prototype.hasOwnProperty()` et la fonction fournie pour déterminer si toutes les clés existent dans le premier objet et ont des valeurs équivalentes.
- Si aucune fonction n'est fournie, les valeurs seront comparées à l'aide de l'opérateur d'égalité.

```js
const matchesWith = (obj, source, fn) =>
  Object.keys(source).every((key) =>
    obj.hasOwnProperty(key) && fn
      ? fn(obj[key], source[key], key, obj, source)
      : obj[key] == source[key]
  );
```

Voici un exemple d'utilisation de cette fonction :

```js
const isGreeting = (val) => /^h(?:i|ello)$/.test(val);
matchesWith(
  { greeting: "hello" },
  { greeting: "hi" },
  (oV, sV) => isGreeting(oV) && isGreeting(sV)
); // true
```

Cet exemple vérifie si les deux objets ont des valeurs équivalentes pour la propriété `greeting`. Il utilise la fonction `isGreeting` pour s'assurer que les deux valeurs sont des salutations valides.
