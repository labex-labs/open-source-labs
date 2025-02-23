# Comment convertir les tabulations en espaces en JavaScript

Pour convertir les caractères de tabulation en espaces lors de la programmation, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `String.prototype.replace()` avec une expression régulière et `String.prototype.repeat()` pour remplacer chaque caractère de tabulation par le nombre d'espaces souhaité.
3. Le extrait de code ci-dessous montre comment utiliser la fonction `expandTabs` pour remplacer les tabulations par des espaces :

```js
const expandTabs = (str, count) => str.replace(/\t/g, " ".repeat(count));

expandTabs("\t\tlorem", 3); // '      lorem'
```

Dans l'exemple ci-dessus, la fonction `expandTabs` prend deux arguments : une chaîne de caractères `str` qui contient des tabulations et un nombre `count` qui représente le nombre d'espaces pour remplacer chaque caractère de tabulation. La fonction utilise la méthode `String.prototype.replace()` avec une expression régulière (`/\t/g`) pour trouver tous les caractères de tabulation dans la chaîne d'entrée et les remplacer par le nombre d'espaces souhaité en utilisant la méthode `String.prototype.repeat()`.
