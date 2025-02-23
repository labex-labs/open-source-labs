# Fonction de formatage de nombres

Pour formater un nombre en utilisant l'ordre de formatage des nombres locaux, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Number.prototype.toLocaleString()` pour convertir un nombre en utilisant les séparateurs de format de nombre locaux.
3. Passez le nombre que vous voulez formater en tant qu'argument à la fonction.

Voici une implémentation d'exemple :

```js
const formatNumber = (num) => num.toLocaleString();
```

Et voici quelques exemples d'utilisation de la fonction :

```js
formatNumber(123456); // '123,456' en `en-US`
formatNumber(15675436903); // '15.675.436.903' en `de-DE`
```
