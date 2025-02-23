# Voici comment trier les caractères d'une chaîne de caractères :

Utilisez le code suivant pour trier les caractères d'une chaîne de caractères par ordre alphabétique :

```js
const sortCharactersInString = (str) =>
  [...str].sort((a, b) => a.localeCompare(b)).join("");
```

Pour commencer, ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

Utilisation de l'exemple :

```js
sortCharactersInString("cabbage"); // 'aabbceg'
```
