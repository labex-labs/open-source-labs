# Algorithme du plus grand sous-tableau

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Cet algorithme trouve un sous-tableau contigu avec la plus grande somme dans un tableau de nombres. Pour implémenter cet algorithme, suivez ces étapes :

- Utilisez une approche gourmande pour suivre la somme actuelle et la somme maximale actuelle, `maxSum`. Initialisez `maxSum` à `-Infinity` pour vous assurer que la plus haute valeur négative est renvoyée si toutes les valeurs sont négatives.
- Définissez des variables pour suivre l'index de début maximal, `sMax`, l'index de fin maximal, `eMax` et l'index de début actuel, `s`.
- Utilisez `Array.prototype.forEach()` pour itérer sur les valeurs et ajoutez la valeur actuelle à la `sum`.
- Si la somme actuelle est supérieure à `maxSum`, mettez à jour les valeurs d'index et la `maxSum`.
- Si la `sum` est inférieure à `0`, réinitialisez-la à `0` et mettez à jour la valeur de `s` avec l'index suivant.
- Utilisez `Array.prototype.slice()` pour renvoyer le sous-tableau indiqué par les variables d'index.

Voici le code JavaScript pour l'algorithme :

```js
const maxSubarray = (...arr) => {
  let maxSum = -Infinity,
    sum = 0;
  let sMax = 0,
    eMax = arr.length - 1,
    s = 0;

  arr.forEach((n, i) => {
    sum += n;
    if (maxSum < sum) {
      maxSum = sum;
      sMax = s;
      eMax = i;
    }

    if (sum < 0) {
      sum = 0;
      s = i + 1;
    }
  });

  return arr.slice(sMax, eMax + 1);
};
```

Voici un exemple d'utilisation de la fonction :

```js
maxSubarray(-2, 1, -3, 4, -1, 2, 1, -5, 4); // [4, -1, 2, 1]
```
