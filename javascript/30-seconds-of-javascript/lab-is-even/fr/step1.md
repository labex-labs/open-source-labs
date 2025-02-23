# Vérifier si un nombre est pair

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Utilisez le code suivant pour vérifier si un nombre est pair ou impair :

```js
const isEven = (num) => num % 2 === 0;
```

Le code ci-dessus utilise l'opérateur modulo (`%`) pour vérifier si un nombre est impair ou pair. Si le nombre est pair, la fonction renvoie `true`. Si c'est impair, la fonction renvoie `false`.

Voici un exemple d'utilisation de la fonction `isEven` :

```js
isEven(3); // renvoie false
```
