# Fonction pour vérifier si une chaîne de caractères est une URL absolue

Pour vérifier si une chaîne de caractères donnée est une URL absolue, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `RegExp.prototype.test()` pour tester si la chaîne de caractères est une URL absolue.
3. La fonction devrait être définie comme suit : `const isAbsoluteURL = str => /^[a-z][a-z0-9+.-]*:/.test(str);`
4. La fonction prend un argument de chaîne de caractères `str` et renvoie `true` si la chaîne de caractères est une URL absolue, et `false` sinon.
5. Testez la fonction à l'aide des exemples fournis :

```js
isAbsoluteURL("https://google.com"); // true
isAbsoluteURL("ftp://www.myserver.net"); // true
isAbsoluteURL("/foo/bar"); // false
```
