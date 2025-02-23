# Voici un conseil sur la manière de compresser et de joindre un tableau

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Voici comment éliminer les valeurs fausses d'un tableau et combiner les valeurs restantes en une chaîne de caractères :

- Utilisez `Array.prototype.filter()` pour filtrer les valeurs fausses telles que `false`, `null`, `0`, `""`, `undefined` et `NaN`.
- Utilisez `Array.prototype.join()` pour joindre les valeurs restantes en une chaîne de caractères.

```js
const compactJoin = (arr, delim = ",") => arr.filter(Boolean).join(delim);
```

Ensuite, appelez la fonction et passez un tableau en tant qu'argument :

```js
compactJoin(["a", "", "b", "c"]); // 'a,b,c'
```
