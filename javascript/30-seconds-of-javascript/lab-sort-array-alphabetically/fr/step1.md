# Comment trier un tableau par ordre alphabétique sur une propriété donnée en JavaScript

Pour trier un tableau d'objets par ordre alphabétique sur une propriété donnée en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.sort()` pour trier le tableau sur la propriété donnée.
3. Utilisez `String.prototype.localeCompare()` pour comparer les valeurs de la propriété donnée.

Voici un extrait de code d'exemple que vous pouvez utiliser :

```js
const alphabetical = (arr, getter, order = "asc") =>
  arr.sort(
    order === "desc"
      ? (a, b) => getter(b).localeCompare(getter(a))
      : (a, b) => getter(a).localeCompare(getter(b))
  );
```

Vous pouvez appeler la fonction `alphabetical` avec un tableau d'objets et la fonction getter qui renvoie la propriété sur laquelle trier. Voici un exemple d'utilisation :

```js
const people = [{ name: "John" }, { name: "Adam" }, { name: "Mary" }];
alphabetical(people, (g) => g.name);
// [ { name: 'Adam' }, { name: 'John' }, { name: 'Mary' } ]
alphabetical(people, (g) => g.name, "desc");
// [ { name: 'Mary' }, { name: 'John' }, { name: 'Adam' } ]
```
