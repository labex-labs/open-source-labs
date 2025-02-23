# Instructions for Converting Map to Object in JavaScript

Pour convertir une `Map` JavaScript en un objet, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Map.prototype.entries()` pour convertir la `Map` en un tableau de paires clé-valeur.
3. Utilisez la méthode `Object.fromEntries()` pour convertir le tableau en un objet.

Voici un extrait de code d'exemple pour convertir une `Map` en un objet :

```js
const mapToObject = (map) => Object.fromEntries(map.entries());
```

Pour tester la fonction, vous pouvez exécuter :

```js
mapToObject(
  new Map([
    ["a", 1],
    ["b", 2]
  ])
); // {a: 1, b: 2}
```
