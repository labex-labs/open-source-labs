# Comment sérialiser un cookie

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Ensuite, suivez ces étapes pour sérialiser une paire nom-valeur de cookie en une chaîne d'en-tête Set-Cookie :

1. Utilisez des littéraux de gabarit et `encodeURIComponent()` pour créer la chaîne appropriée.
2. Implémentez la fonction `serializeCookie` en passant les paramètres `name` et `val`.
3. La fonction retournera une chaîne correctement sérialisée.

Voici un exemple d'utilisation de la fonction `serializeCookie` :

```js
const serializeCookie = (name, val) =>
  `${encodeURIComponent(name)}=${encodeURIComponent(val)}`;

serializeCookie("foo", "bar"); // 'foo=bar'
```

Dans cet exemple, la fonction `serializeCookie` prend `foo` comme nom de cookie et `bar` comme valeur de cookie, et retourne une chaîne de cookie sérialisée de `foo=bar`.
