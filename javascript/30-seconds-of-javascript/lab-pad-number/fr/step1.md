# Comment ajouter des caractères avant un nombre en JavaScript

Pour ajouter des caractères avant un nombre en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `String.prototype.padStart()` pour ajouter des caractères au nombre jusqu'à la longueur spécifiée, après l'avoir converti en chaîne de caractères.
3. La fonction `padNumber()` ci-dessous illustre cette approche.
4. Passez le nombre et la longueur souhaitée en tant qu'arguments à la fonction.
5. La fonction renvoie le nombre avec des caractères ajoutés sous forme de chaîne de caractères.

```js
const padNumber = (n, l) => `${n}`.padStart(l, "0");
```

Utilisation de l'exemple :

```js
padNumber(1234, 6); // '001234'
```
