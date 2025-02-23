# Vérificateur de propriété

Pour vérifier si une propriété spécifique d'un objet répond à une certaine condition, utilisez la fonction `checkProp`. Cette fonction crée une fonction curryée qui prend une fonction prédicat et un nom de propriété en arguments. La fonction renvoyée prend ensuite un objet et renvoie `true` ou `false` selon que la propriété spécifiée répond ou non à la condition spécifiée par la fonction prédicat.

Voici une implémentation de `checkProp` :

```js
const checkProp = (predicate, prop) => (obj) => !!predicate(obj[prop]);
```

Voici quelques exemples d'utilisation :

```js
const lengthIs4 = checkProp((l) => l === 4, "length");
lengthIs4([]); // false
lengthIs4([1, 2, 3, 4]); // true
lengthIs4(new Set([1, 2, 3, 4])); // false (Set utilise Size, pas length)

const session = { user: {} };
const validUserSession = checkProp((u) => u.active && !u.disabled, "user");

validUserSession(session); // false

session.user.active = true;
validUserSession(session); // true

const noLength = checkProp((l) => l === undefined, "length");
noLength([]); // false
noLength({}); // true
noLength(new Set()); // true
```

En résumé, la fonction `checkProp` vous permet de vérifier facilement la valeur d'une propriété spécifique sur un objet en spécifiant une fonction prédicat pour cette propriété.
