# Fonction pour Copier le Signe d'un Nombre sur un Autre

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

La fonction `copySign` renvoie la valeur absolue du premier nombre, mais avec le signe du second nombre. Pour y arriver :

1. Utilisez `Math.sign()` pour vérifier si les deux nombres ont le même signe.
2. Retournez `x` si c'est le cas, `-x` sinon.

Voici le code pour la fonction `copySign` :

```js
const copySign = (x, y) => (Math.sign(x) === Math.sign(y) ? x : -x);
```

Vous pouvez tester la fonction à l'aide du code suivant :

```js
copySign(2, 3); // 2
copySign(2, -3); // -2
copySign(-2, 3); // 2
copySign(-2, -3); // -2
```
