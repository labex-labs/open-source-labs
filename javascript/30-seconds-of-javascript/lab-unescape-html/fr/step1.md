# Déséchapper le HTML

Cette fonction déséchappe les caractères HTML échappés. Pour l'utiliser, suivez ces étapes :

1. Ouvrez le Terminal/SSH.
2. Tapez `node`.
3. Copiez et collez le code suivant :

```js
const unescapeHTML = (str) =>
  str.replace(
    /&amp;|&lt;|&gt;|&#39;|&quot;/g,
    (tag) =>
      ({
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "&#39;": "'",
        "&quot;": '"'
      })[tag] || tag
  );
```

4. Appelez la fonction `unescapeHTML` et passez-lui une chaîne de caractères avec des caractères échappés.
5. La fonction renverra la chaîne de caractères déséchappée.

Utilisation exemple :

```js
unescapeHTML("&lt;a href=&quot;#&quot;&gt;Me &amp; you&lt;/a&gt;");
// '<a href="#">Me & you</a>'
```
