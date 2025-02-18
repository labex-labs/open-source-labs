# Conversion d'un entier en chiffres romains

Pour convertir un entier en sa représentation en chiffres romains, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

2. La fonction `toRomanNumeral()` accepte les valeurs comprises entre `1` et `3999` (les deux inclus).

3. Créez une table de correspondance (lookup table) contenant des tableaux à 2 valeurs sous la forme (valeur romaine, entier).

4. Utilisez `Array.prototype.reduce()` pour parcourir les valeurs dans `lookup` et diviser répétitivement `num` par la valeur.

5. Utilisez `String.prototype.repeat()` pour ajouter la représentation en chiffres romains à l'accumulateur.

Voici le code de la fonction `toRomanNumeral()` :

```js
const toRomanNumeral = (num) => {
  const lookup = [
    ["M", 1000],
    ["CM", 900],
    ["D", 500],
    ["CD", 400],
    ["C", 100],
    ["XC", 90],
    ["L", 50],
    ["XL", 40],
    ["X", 10],
    ["IX", 9],
    ["V", 5],
    ["IV", 4],
    ["I", 1]
  ];
  return lookup.reduce((acc, [k, v]) => {
    acc += k.repeat(Math.floor(num / v));
    num = num % v;
    return acc;
  }, "");
};
```

Vous pouvez tester la fonction avec ces exemples :

```js
toRomanNumeral(3); // 'III'
toRomanNumeral(11); // 'XI'
toRomanNumeral(1998); // 'MCMXCVIII'
```
