# Fonction de validation de nombre

Pour valider si une entrée donnée est un nombre, suivez ces étapes :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Utilisez `parseFloat()` pour essayer de convertir l'entrée en nombre.
- Utilisez `Number.isNaN()` et l'opérateur logique non (`!`) pour vérifier si l'entrée est un nombre.
- Utilisez `Number.isFinite()` pour vérifier si l'entrée est finie.
- Utilisez `Number` et l'opérateur d'égalité large (`==`) pour vérifier si la coercition est valide.

Voici le code pour la fonction `validateNumber` :

```js
const validateNumber = (input) => {
  const num = parseFloat(input);
  return !Number.isNaN(num) && Number.isFinite(num) && Number(input) == input;
};
```

Vous pouvez utiliser la fonction `validateNumber` comme suit :

```js
validateNumber("10"); // true
validateNumber("a"); // false
```
