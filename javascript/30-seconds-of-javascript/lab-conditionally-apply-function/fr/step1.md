# Utilisation de la fonction when pour appliquer une condition

Pour appliquer une fonction lorsqu'une certaine condition est remplie, utilisez la fonction `when`. Pour commencer, ouvrez le Terminal/SSH et tapez `node`.

La fonction `when` renvoie une nouvelle fonction qui prend un argument et exécute un rappel si l'argument est évalué comme vrai, ou renvoie l'argument s'il est évalué comme faux. La fonction attend une seule valeur, `x`, et renvoie la valeur appropriée en fonction du paramètre `pred`.

Voici une implémentation de l'exemple de la fonction `when` :

```js
const when = (pred, whenTrue) => (x) => (pred(x) ? whenTrue(x) : x);
```

Vous pouvez utiliser la fonction `when` pour créer une nouvelle fonction qui double les nombres pairs :

```js
const doubleEvenNumbers = when(
  (x) => x % 2 === 0,
  (x) => x * 2
);
doubleEvenNumbers(2); // 4
doubleEvenNumbers(1); // 1
```
