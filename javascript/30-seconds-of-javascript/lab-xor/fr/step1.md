# Ou exclusif logique

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. L'ou exclusif logique vérifie si seulement l'un des arguments est `true`. Pour créer l'ou exclusif logique, utilisez les opérateurs ou logique (`||`), et (`&&`) et non (`!`) sur les deux valeurs données. Voici un exemple de code pour cela :

```js
const xor = (a, b) => (a || b) && !(a && b);
```

Voici les valeurs de sortie :

```js
xor(true, true); // false
xor(true, false); // true
xor(false, true); // true
xor(false, false); // false
```
