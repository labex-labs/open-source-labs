# Voici comment convertir un objet en Map

Pour convertir un objet en un `Map`, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Object.entries()` pour convertir l'objet en un tableau de paires clé-valeur.
3. Utilisez le constructeur `Map` pour convertir le tableau en un `Map`.

Voici un extrait de code d'exemple :

```js
const objectToMap = (obj) => new Map(Object.entries(obj));
```

Vous pouvez utiliser la fonction `objectToMap()` pour convertir un objet en un `Map`. Par exemple :

```js
objectToMap({ a: 1, b: 2 }); // Map {'a' => 1, 'b' => 2}
```
