# Fonction pour vérifier si un nombre est premier

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Cette fonction vérifie si un entier donné est un nombre premier. Voici les étapes pour vérifier si un nombre est premier :

1. Vérifiez les nombres de `2` jusqu'à la racine carrée du nombre donné.
2. Si l'un d'entre eux divise le nombre donné, renvoyez `false`.
3. Si aucun d'entre eux ne divise le nombre donné, renvoyez `true`, sauf si le nombre est inférieur à `2`.

Voici le code pour implémenter cette fonction en JavaScript :

```js
const isPrime = (num) => {
  const boundary = Math.floor(Math.sqrt(num));
  for (let i = 2; i <= boundary; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return num >= 2;
};
```

Vous pouvez tester la fonction en l'appelant avec un nombre en argument :

```js
isPrime(11); // true
```
