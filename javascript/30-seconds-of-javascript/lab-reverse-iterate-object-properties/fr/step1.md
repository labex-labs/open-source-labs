# Voici comment itérer sur les propriétés propres d'un objet dans l'ordre inverse

Pour itérer sur les propriétés propres d'un objet dans l'ordre inverse et exécuter une fonction de rappel pour chacune d'entre elles, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Object.keys()` pour obtenir toutes les propriétés de l'objet.
3. Utilisez `Array.prototype.reverse()` pour inverser l'ordre des propriétés.
4. Utilisez `Array.prototype.forEach()` pour exécuter la fonction fournie pour chaque paire clé-valeur.
5. La fonction de rappel devrait avoir trois arguments : la valeur, la clé et l'objet.

Voici le code :

```js
const forOwnRight = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .forEach((key) => fn(obj[key], key, obj));
```

Vous pouvez utiliser cette fonction avec n'importe quel objet et fonction de rappel. Par exemple, pour afficher les valeurs de `{ foo: 'bar', a: 1 }` dans l'ordre inverse, vous pouvez utiliser le code suivant :

```js
forOwnRight({ foo: "bar", a: 1 }, (v) => console.log(v)); // 1, 'bar'
```
