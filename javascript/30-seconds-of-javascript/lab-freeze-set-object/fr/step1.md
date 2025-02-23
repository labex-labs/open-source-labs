# Création d'un objet Set congelé en JavaScript

Pour créer un objet `Set` congelé en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez le constructeur `Set` pour créer un nouvel objet `Set` à partir d'un `itérable`.
3. Définissez les méthodes `add`, `delete` et `clear` de l'objet nouvellement créé sur `undefined` pour geler efficacement l'objet.

Voici un extrait de code d'exemple :

```js
const frozenSet = (iterable) => {
  const s = new Set(iterable);
  s.add = undefined;
  s.delete = undefined;
  s.clear = undefined;
  return s;
};

console.log(frozenSet([1, 2, 3, 1, 2]));
// Sortie : Set { 1, 2, 3, add: undefined, delete: undefined, clear: undefined }
```

Ce code crée un objet `Set` congelé à partir d'un itérable de nombres et renvoie l'objet avec ses méthodes `add`, `delete` et `clear` définies sur `undefined`.
