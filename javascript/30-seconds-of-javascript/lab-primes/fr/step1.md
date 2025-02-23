# Générer des nombres premiers en utilisant le crible d'Ératosthène

Pour générer des nombres premiers jusqu'à un nombre donné en utilisant le crible d'Ératosthène, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Créez un tableau contenant les nombres de `2` au nombre donné.
3. Utilisez `Array.prototype.filter()` pour filtrer les valeurs qui sont divisibles par tout nombre de `2` à la racine carrée du nombre fourni.
4. Retournez le tableau résultant contenant les nombres premiers.

Voici le code JavaScript pour générer des nombres premiers jusqu'à un nombre donné :

```js
const generatePrimes = (num) => {
  let arr = Array.from({ length: num - 1 }).map((x, i) => i + 2),
    sqrt = Math.floor(Math.sqrt(num)),
    numsTillSqrt = Array.from({ length: sqrt - 1 }).map((x, i) => i + 2);
  numsTillSqrt.forEach(
    (x) => (arr = arr.filter((y) => y % x !== 0 || y === x))
  );
  return arr;
};
```

Vous pouvez appeler la fonction `generatePrimes()` en passant le nombre souhaité en tant qu'argument. Par exemple :

```js
generatePrimes(10); // [2, 3, 5, 7]
```
