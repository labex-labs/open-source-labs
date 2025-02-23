# Comment obtenir le suffixe meridiem d'un entier

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`.

Voici une fonction qui convertit un entier en une chaîne de caractères au format horaire de 12 heures avec un suffixe meridiem.

Pour ce faire, utilisez l'opérateur modulo (`%`) et des vérifications conditionnelles.

```js
const getMeridiemSuffixOfInteger = (num) => {
  if (num === 0 || num === 24) {
    return "12am";
  } else if (num === 12) {
    return "12pm";
  } else if (num < 12) {
    return num + "am";
  } else {
    return (num % 12) + "pm";
  }
};
```

Voici quelques exemples d'utilisation de cette fonction :

```js
getMeridiemSuffixOfInteger(0); // '12am'
getMeridiemSuffixOfInteger(11); // '11am'
getMeridiemSuffixOfInteger(13); // '1pm'
getMeridiemSuffixOfInteger(25); // '1pm'
```

Cette fonction prend un entier en argument et renvoie une chaîne de caractères avec le suffixe meridiem.
