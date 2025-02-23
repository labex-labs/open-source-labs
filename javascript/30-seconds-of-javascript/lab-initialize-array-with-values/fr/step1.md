# Fonction pour initialiser un tableau avec des valeurs spécifiées

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Cette fonction initialise un tableau avec les valeurs spécifiées :

- Utilisez le constructeur `Array()` pour créer un tableau de la longueur souhaitée.
- Utilisez `Array.prototype.fill()` pour le remplir avec les valeurs souhaitées.
- Si aucune valeur n'est spécifiée, elle prend la valeur par défaut `0`.

```js
const initializeArrayWithValues = (length, value = 0) =>
  Array(length).fill(value);
```

Utilisation exemple :

```js
initializeArrayWithValues(5, 2); // [2, 2, 2, 2, 2]
```
