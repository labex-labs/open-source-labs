# Vérification de Luhn

Pour utiliser l'algorithme de Luhn pour la validation de numéros d'identification, tels que les numéros de carte de crédit, les numéros IMEI, les numéros d'identifiant de fournisseur national, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez les méthodes suivantes : `String.prototype.split()`, `Array.prototype.reverse()`, `Array.prototype.map()` et `parseInt()` en combinaison pour obtenir un tableau de chiffres.
3. Utilisez `Array.prototype.shift()` pour obtenir le dernier chiffre.
4. Utilisez `Array.prototype.reduce()` pour implémenter l'algorithme de Luhn.
5. Retournez `true` si `sum` est divisible par `10`, `false` sinon.

Voici le code :

```js
const luhnCheck = (num) => {
  const arr = (num + "")
    .split("")
    .reverse()
    .map((x) => parseInt(x));
  const lastDigit = arr.shift();
  let sum = arr.reduce(
    (acc, val, i) =>
      i % 2 !== 0 ? acc + val : acc + ((val *= 2) > 9 ? val - 9 : val),
    0
  );
  sum += lastDigit;
  return sum % 10 === 0;
};
```

Vous pouvez tester la fonction de vérification de Luhn à l'aide de ces exemples :

```js
luhnCheck("4485275742308327"); // true
luhnCheck(6011329933655299); //  true
luhnCheck(123456789); // false
```
